import flet as ft
from flet import UserControl
from pages.chat import stream_chat


class MessagesPage(ft.UserControl):
    def __init__(self, page: ft.Page, go_to):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.channel_id = "general"

        self.page.title = "Messages"
        self.page.padding = 0
        self.page.scroll = "adaptive"
        self.page.bgcolor = "#F8F9FA"

        self.set_mobile_view()
        self.page.on_resize = self.adjust_window_size
        self.adjust_window_size()

        self.header_section = ft.Container(
            content=ft.Row(
                [
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        icon_size=24,
                        bgcolor="transparent",
                        on_click=lambda e: self.go_to("/homepage", page),
                    ),
                    ft.Text("Messages", size=18, weight="bold"),
                ],
                alignment="start",
                vertical_alignment="center",
            ),
            padding=15,
        )

        self.search_section = ft.Container(
            content=ft.TextField(
                hint_text="Search",
                prefix_icon=ft.icons.SEARCH,
                expand=True,
                border_radius=5,
            ),
            padding=15,
        )

        self.filter_section = ft.Container(
            content=ft.Row(
                [
                    ft.ElevatedButton(
                        "All", expand=True, color="white", bgcolor="#6200EE"
                    ),
                    ft.ElevatedButton("Direct", expand=True, color="black"),
                    ft.ElevatedButton("Group Chat", expand=True, color="black"),
                ],
                alignment="spaceEvenly",
            ),
            padding=15,
        )

        self.messages_column = ft.Column()
        self.load_messages()

        self.message_input = ft.TextField(
            hint_text="Type a message...",
            expand=True,
            border_radius=5,
            on_submit=self.send_message,
        )

        self.send_button = ft.IconButton(icon=ft.icons.SEND, on_click=self.send_message)

        self.input_section = ft.Row(
            [self.message_input, self.send_button], alignment="spaceBetween"
        )

        self.messages_section = ft.Container(content=self.messages_column, padding=15)

        self.main_content = ft.ListView(
            controls=[
                self.header_section,
                self.search_section,
                self.filter_section,
                self.messages_section,
                self.input_section,
            ],
            expand=True,
            padding=ft.padding.all(16),
        )

        self.bottom_nav = ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        content=ft.Image(src="images/Home.png", width=24, height=24),
                        icon_size=24,
                        on_click=lambda _: self.go_to("/homepage", page),
                    ),
                    ft.IconButton(
                        content=ft.Image(src="images/Star.png", width=24, height=24),
                        icon_size=24,
                        on_click=lambda _: self.go_to("/bookings", page),
                    ),
                    ft.IconButton(
                        content=ft.Image(src="images/Message.png", width=24, height=24),
                        icon_size=24,
                        on_click=lambda e: self.go_to("/messages", page),
                    ),
                    ft.IconButton(
                        content=ft.Image(src="images/Profile.png", width=24, height=24),
                        icon_size=24,
                        on_click=lambda e: self.go_to("/profile", page),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            bgcolor="#FFFFFF",
            border_radius=30,
        )

        self.page.controls.append(self.main_content)
        self.page.controls.append(self.bottom_nav)

        self.page.update()

        print("MessagesPage initialized")

    def load_messages(self):
        messages = stream_chat.get_messages(self.channel_id)
        print("Loaded messages:", messages)
        self.messages_column.controls.clear()
        for msg in messages:
            print("Processing message:", msg)
            self.messages_column.controls.append(
                self.message_item(
                    msg.get("user_id", "Unknown"),
                    msg.get("text", ""),
                    msg.get("created_at", ""),
                )
            )
        self.page.update()

    def send_message(self, e):
        message_text = self.message_input.value.strip()
        if message_text:
            stream_chat.send_message(self.channel_id, message_text)
            self.message_input.value = ""
            self.load_messages()
        self.page.update()

    def message_item(self, sender, message, time):
        sender_name = sender if sender else "Unknown"
        message_text = message if message else "(No Message)"
        timestamp = time if time else "Unknown Time"

        return ft.Container(
            padding=10,
            content=ft.Row(
                [
                    ft.Icon(ft.icons.PERSON, size=40, color="#6200EE"),
                    ft.Column(
                        [
                            ft.Text(sender_name, weight="bold", size=14),
                            ft.Text(message_text, size=12, color="gray"),
                        ],
                        spacing=2,
                        expand=True,
                    ),
                    ft.Text(timestamp, size=12, color="gray"),
                ],
                alignment="spaceBetween",
            ),
        )

    def set_mobile_view(self):
        self.page.window_width = 400
        self.page.window_height = 680

    def adjust_window_size(self, _=None):
        screen_width = self.page.window_width
        screen_height = self.page.window_height

        if screen_width <= 480:
            self.set_mobile_view()
        elif 481 <= screen_width <= 1024:
            self.page.window_width = min(screen_width, 800)
            self.page.window_height = min(screen_height, 1000)
        else:
            self.page.window_width = min(screen_width, 1200)
            self.page.window_height = min(screen_height, 900)
        self.page.update()
