import flet as ft
from flet import UserControl
from pages.chat import stream_chat
import asyncio
import urllib.parse


class ConversationPage(UserControl):
    def __init__(self, page: ft.Page, go_to, channel_id=None, contact_name=""):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.channel_id = channel_id or "general"
        self.contact_name = (
            urllib.parse.unquote(contact_name) if contact_name else "Unknown"
        )
        self.messages_column = ft.Column()

        self.page.title = f"Chat with {self.contact_name}"
        self.page.padding = 0
        self.page.scroll = "adaptive"
        self.page.bgcolor = "#F8F9FA"

        self.header_section = ft.Container(
            content=ft.Row(
                [
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        icon_size=24,
                        on_click=lambda e: self.go_to("/messages", self.page),
                    ),
                    ft.Text(self.contact_name, size=18, weight="bold"),
                ],
                alignment="start",
                vertical_alignment="center",
            ),
            padding=15,
        )

        self.messages_section = ft.Container(content=self.messages_column, padding=15)

        self.input_field = ft.TextField(
            hint_text="Type a message...",
            expand=True,
            border_radius=5,
            on_submit=self.send_message,
        )

        self.send_button = ft.IconButton(
            icon=ft.icons.SEND,
            icon_size=24,
            on_click=self.send_message,
        )

        self.input_section = ft.Container(
            content=ft.Row(
                [self.input_field, self.send_button], alignment="spaceBetween"
            ),
            padding=15,
        )

        self.main_content = ft.ListView(
            controls=[
                self.header_section,
                self.messages_section,
                self.input_section,
            ],
            expand=True,
            padding=ft.padding.all(16),
        )

    async def did_mount(self):

        await self.load_messages()

    async def load_messages(self):
        messages = await asyncio.to_thread(stream_chat.get_messages, self.channel_id)
        self.messages_column.controls.clear()

        for msg in messages:
            self.messages_column.controls.append(
                self.message_item(
                    sender=msg.get("user", {}).get("id", "Unknown"),
                    message=msg.get("text", ""),
                    time=msg.get("created_at", ""),
                )
            )
        self.page.update()

    async def send_message(self, e):
        message_text = self.input_field.value.strip()
        if message_text:
            success = await asyncio.to_thread(
                stream_chat.send_message, self.channel_id, message_text
            )
            if success:
                self.input_field.value = ""
                await self.load_messages()
        self.page.update()

    def message_item(self, sender, message, time):
        return ft.Container(
            padding=10,
            content=ft.Row(
                [
                    ft.Icon(ft.icons.PERSON, size=40, color="#6200EE"),
                    ft.Column(
                        [
                            ft.Text(sender, weight="bold", size=14),
                            ft.Text(message, size=12, color="gray"),
                        ],
                        spacing=2,
                        expand=True,
                    ),
                    ft.Text(time, size=12, color="gray"),
                ],
                alignment="spaceBetween",
            ),
        )

    def build(self):
        return ft.Column(
            [
                ft.Container(content=self.main_content, expand=True),
            ]
        )
