import flet as ft
from flet import UserControl
from pages.chat import stream_chat
import asyncio


class MessagesPage(UserControl):
    def __init__(self, page: ft.Page, go_to):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.channel_id = "general"
        self.chat_type = "all"

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
                        on_click=lambda e: self.go_to("/homepage", self.page),
                    ),
                    ft.Text("Messages", size=18, weight="bold"),
                ],
                alignment="start",
                vertical_alignment="center",
            ),
            padding=15,
        )

        self.search_section = ft.Container(
            content=ft.Row(
                [
                    ft.TextField(
                        hint_text="Search",
                        prefix_icon=ft.icons.SEARCH,
                        expand=True,
                        border_radius=5,
                    ),
                    ft.IconButton(
                        icon=ft.icons.CREATE_OUTLINED,
                        icon_size=24,
                        on_click=lambda e: self.go_to("/newmessages", self.page),
                    ),
                ],
                alignment="spaceBetween",
            ),
            padding=15,
        )

        self.all_button = ft.ElevatedButton(
            "All",
            expand=True,
            color="white",
            bgcolor="#6200EE",
            on_click=lambda e: self.set_chat_type("all"),
        )
        self.direct_button = ft.ElevatedButton(
            "Direct",
            expand=True,
            color="black",
            bgcolor="white",
            on_click=lambda e: self.set_chat_type("direct"),
        )
        self.group_chat_button = ft.ElevatedButton(
            "Group Chat",
            expand=True,
            color="black",
            bgcolor="white",
            on_click=lambda e: self.set_chat_type("group"),
        )

        self.filter_section = ft.Container(
            content=ft.Row(
                [self.all_button, self.direct_button, self.group_chat_button],
                alignment="spaceEvenly",
            ),
            padding=15,
        )

        self.messages_column = ft.Column()
        self.messages_section = ft.Container(content=self.messages_column, padding=15)

        self.main_content = ft.ListView(
            controls=[
                self.header_section,
                self.search_section,
                self.filter_section,
                self.messages_section,
            ],
            expand=True,
            padding=ft.padding.all(16),
        )

        self.bottom_nav = ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        content=ft.Image(
                            src="images/Home.png",
                            width=24,
                            height=24,
                        ),
                        icon_size=24,
                        icon_color="#000000",
                        on_click=lambda _: self.go_to("/homepage", self.page),
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src="images/Star.png",
                            width=24,
                            height=24,
                        ),
                        icon_size=24,
                        icon_color="#000000",
                        on_click=lambda _: self.go_to("/bookings", self.page),
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src="images/Message.png",
                            width=24,
                            height=24,
                        ),
                        icon_size=24,
                        icon_color="#000000",
                        on_click=lambda _: self.go_to("/messages", self.page),
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src="images/Profile.png",
                            width=24,
                            height=24,
                        ),
                        icon_size=24,
                        icon_color="#000000",
                        on_click=lambda _: self.go_to("/profile", self.page),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            bgcolor="#FFFFFF",
            border_radius=30,
            padding=ft.padding.symmetric(vertical=10),
        )

        asyncio.run(self.async_load_messages())

    async def async_load_messages(self):
        await self.load_messages()

    def build(self):
        return ft.Column(
            [
                ft.Container(content=self.main_content, expand=True),
                ft.Container(
                    content=self.bottom_nav,
                    alignment=ft.alignment.bottom_center,
                    bgcolor="#FFFFFF",
                    padding=ft.padding.all(10),
                ),
            ]
        )

    async def async_load_messages(self):
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

    def set_chat_type(self, chat_type):
        self.chat_type = chat_type

        self.all_button.bgcolor = "#6200EE" if chat_type == "all" else "white"
        self.all_button.color = "white" if chat_type == "all" else "black"

        self.direct_button.bgcolor = "#6200EE" if chat_type == "direct" else "white"
        self.direct_button.color = "white" if chat_type == "direct" else "black"

        self.group_chat_button.bgcolor = "#6200EE" if chat_type == "group" else "white"
        self.group_chat_button.color = "white" if chat_type == "group" else "black"

        self.all_button.update()
        self.direct_button.update()
        self.group_chat_button.update()

        asyncio.create_task(self.async_load_messages())

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
