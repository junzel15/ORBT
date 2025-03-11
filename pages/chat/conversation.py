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
        self.conversation_list_column = ft.Column()

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

        self.conversation_list_section = ft.Container(
            content=self.conversation_list_column,
            padding=15,
            bgcolor="#EAEAEA",
            height=400,
            width=400,
            border_radius=10,
        )

        self.input_field = ft.TextField(
            hint_text="Message...",
            expand=True,
            border_color="transparent",
            text_size=14,
            bgcolor="transparent",
            content_padding=ft.padding.only(left=0),
        )

        self.input_field_container = ft.Container(
            content=ft.Row(
                [
                    ft.IconButton(
                        icon=ft.icons.CAMERA_ALT,
                        icon_size=20,
                        on_click=self.open_camera,
                        style=ft.ButtonStyle(color="#6200EE"),
                    ),
                    self.input_field,
                    ft.IconButton(
                        icon=ft.icons.MIC,
                        icon_size=20,
                        on_click=self.start_recording,
                        style=ft.ButtonStyle(color="#6200EE"),
                    ),
                    ft.IconButton(
                        icon=ft.icons.IMAGE,
                        icon_size=20,
                        on_click=self.import_image,
                        style=ft.ButtonStyle(color="#6200EE"),
                    ),
                ],
                alignment="spaceBetween",
            ),
            border_radius=30,
            padding=10,
            bgcolor="#EAEAEA",
            expand=True,
        )

        self.send_button = ft.IconButton(
            icon=ft.icons.SEND,
            icon_size=24,
            on_click=self.send_message,
            style=ft.ButtonStyle(color="#6200EE"),
        )

        self.input_section = ft.Container(
            content=ft.Row(
                [
                    self.input_field_container,
                    self.send_button,
                ],
                alignment="center",
            ),
            padding=10,
            bgcolor="white",
        )

        self.main_content = ft.ListView(
            controls=[
                self.header_section,
                self.messages_section,
                self.conversation_list_section,
                self.input_section,
            ],
            expand=True,
            padding=ft.padding.all(16),
        )

    def did_mount(self):
        self.page.run_task(self.load_messages)

    async def load_messages(self):
        messages = await asyncio.to_thread(stream_chat.get_messages, self.channel_id)
        self.messages_column.controls.clear()
        self.conversation_list_column.controls.clear()

        for msg in messages:
            self.add_message_to_ui(
                sender=msg.get("user", {}).get("id", "Unknown"),
                message=msg.get("text", ""),
                time=msg.get("created_at", ""),
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
                self.input_field.update()

                self.add_message_to_ui(
                    sender="You",
                    message=message_text,
                    time="Just now",
                )

    def add_message_to_ui(self, sender, message, time):

        message_item = self.message_item(sender, message, time)
        self.messages_column.controls.append(message_item)

        self.conversation_list_column.controls.append(
            ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(ft.icons.PERSON, size=30, color="#6200EE"),
                        ft.Text(f"{sender}: {message}", size=12),
                    ],
                    alignment="start",
                ),
                padding=10,
                bgcolor="#FFFFFF",
                border_radius=10,
                margin=ft.margin.only(bottom=5),
            )
        )

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
        return self.main_content

    def open_camera(self, e):
        print("Opening camera...")

    def start_recording(self, e):
        print("Starting recording...")

    def import_image(self, e):
        print("Importing image...")
