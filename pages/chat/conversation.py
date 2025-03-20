import flet as ft
from flet import UserControl
from pages.chat import stream_chat
import asyncio
import urllib.parse


class ConversationPage(UserControl):
    def __init__(
        self,
        page: ft.Page,
        go_to,
        channel_id=None,
        contact_name="",
        group_name=None,
        users=None,
    ):
        self.users = users or []
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.channel_id = channel_id or "general"
        self.contact_name = (
            urllib.parse.unquote(contact_name) if contact_name else "Unknown"
        )

        self.page.padding = 0
        self.page.scroll = "adaptive"
        self.page.bgcolor = "#F8F9FA"

        self.group_name = group_name
        self.page.title = f"Chat with {self.group_name or self.contact_name}"

        self.header_section = ft.Container(
            content=ft.Row(
                [
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        icon_size=24,
                        on_click=lambda e: self.go_to("/messages", self.page),
                    ),
                    ft.Text(
                        self.group_name or self.contact_name, size=18, weight="bold"
                    ),
                ],
                alignment="start",
                vertical_alignment="center",
            ),
            padding=15,
        )

        self.messages_list_view = ft.ListView(
            spacing=5,
            padding=5,
            auto_scroll=True,
            expand=True,
        )

        self.messages_section = ft.Container(
            content=self.messages_list_view,
            height=470,
            padding=10,
            bgcolor="#F8F9FA",
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
                    ),
                    self.input_field,
                    ft.IconButton(
                        icon=ft.icons.MIC, icon_size=20, on_click=self.start_recording
                    ),
                    ft.IconButton(
                        icon=ft.icons.IMAGE, icon_size=20, on_click=self.import_image
                    ),
                ],
                alignment="spaceBetween",
                vertical_alignment="center",
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
        )

        self.input_section = ft.Container(
            content=ft.Row(
                [
                    self.input_field_container,
                    self.send_button,
                ],
                alignment="center",
                vertical_alignment="center",
            ),
            height=60,
            padding=5,
            bgcolor="white",
            border_radius=10,
        )

        self.main_content = ft.Column(
            controls=[
                self.header_section,
                self.messages_section,
                self.input_section,
            ],
            expand=True,
            scroll="adaptive",
        )

    def did_mount(self):
        self.page.run_task(self.load_messages)

    async def load_messages(self):
        try:
            messages = await asyncio.to_thread(
                stream_chat.get_messages, self.channel_id
            )

            self.messages_list_view.controls.clear()

            seen_message_ids = set()

            for msg in messages:
                msg_id = msg.get("id")
                if msg_id and msg_id not in seen_message_ids:
                    seen_message_ids.add(msg_id)
                    self.add_message_to_ui(
                        sender=msg.get("user", {}).get("id", "Unknown"),
                        message=msg.get("text", ""),
                        time=msg.get("created_at", ""),
                    )

            self.page.update()

        except Exception as e:
            print(f"Error loading messages: {e}")

    async def send_message(self, e):
        message_text = self.input_field.value.strip()

        if message_text:
            try:
                print(f"Attempting to send message: {message_text}")

                user_id, _ = stream_chat.get_authenticated_user()
                response = await asyncio.to_thread(
                    stream_chat.send_message, self.channel_id, message_text
                )

                if response and "message" in response:
                    sent_message = response["message"]
                    self.add_message_to_ui(
                        sender="You",
                        message=sent_message["text"],
                        time="Just now",
                    )

                    self.input_field.value = ""
                    self.input_field.update()

                    self.messages_section.update()
                    self.page.update()

                else:
                    print("Failed to send message to stream.")

            except Exception as e:
                print(f"Error sending message: {e}")

    def add_message_to_ui(self, sender, message, time):
        print(f"Adding message to UI: {sender}: {message}")
        message_item = self.message_item(sender, message, time)
        self.messages_list_view.controls.append(message_item)

        self.messages_list_view.auto_scroll = True
        self.messages_list_view.update()

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
