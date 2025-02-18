import flet as ft
from flet import UserControl


class MessagesPage(ft.UserControl):
    def __init__(self, page: ft.Page, go_to):
        super().__init__()
        self.page = page
        self.go_to = go_to

        self.page.title = "Messages"
        self.page.padding = 0
        self.page.scroll = "adaptive"
        self.page.bgcolor = "#F8F9FA"

        self.header_section = ft.Container(
            content=ft.Row(
                [
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        icon_size=24,
                        bgcolor="transparent",
                        on_click=lambda e: self.go_to("/homepage", page),
                    ),
                    ft.Text(
                        "Messages",
                        size=18,
                        weight="bold",
                    ),
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

        self.messages_section = ft.Container(
            content=ft.Column(
                controls=[
                    self.message_item(
                        ft.icons.EVENT,
                        "Event: BRO001",
                        "ORB: The countdown is over - Let the...",
                        "Exp: 4hrs",
                        color="#6200EE",
                    ),
                    self.message_item(
                        ft.icons.EVENT,
                        "Event: BAO001",
                        "Inka: On my way guys, See you!",
                        "Exp: 4hrs",
                        color="#6200EE",
                    ),
                    self.message_item(
                        ft.icons.FAVORITE,
                        "Event: EXO001",
                        "You: See you!",
                        "Exp: 4hrs",
                        color="#6200EE",
                    ),
                ]
            ),
            padding=15,
        )

        is_mobile = self.page.window_width < 600
        self.bottom_nav = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.IconButton(
                            content=ft.Image(
                                src="images/Home.png",
                                width=(24 if not is_mobile else 20),
                                height=(24 if not is_mobile else 20),
                            ),
                            icon_size=24,
                            icon_color="#000000",
                            on_click=lambda _: self.go_to("/homepage", page),
                        ),
                    ),
                    ft.Container(
                        content=ft.IconButton(
                            content=ft.Image(
                                src="images/Star.png",
                                width=(24 if not is_mobile else 20),
                                height=(24 if not is_mobile else 20),
                            ),
                            icon_size=24,
                            icon_color="#000000",
                            on_click=lambda _: self.go_to("/bookings", page),
                        ),
                    ),
                    ft.Container(
                        content=ft.IconButton(
                            content=ft.Image(
                                src="images/Message.png",
                                width=(24 if not is_mobile else 20),
                                height=(24 if not is_mobile else 20),
                            ),
                            icon_size=24,
                            icon_color="#000000",
                            on_click=lambda e: self.go_to("/messages", page),
                        ),
                    ),
                    ft.Container(
                        content=ft.IconButton(
                            content=ft.Image(
                                src="images/Profile.png",
                                width=(24 if not is_mobile else 20),
                                height=(24 if not is_mobile else 20),
                            ),
                            icon_size=24,
                            icon_color="#000000",
                            on_click=lambda e: self.go_to("/profile", page),
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            bgcolor="#FFFFFF",
            border_radius=30,
        )

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

    def message_item(self, icon, name, message, time, color="white"):
        return ft.Container(
            padding=10,
            content=ft.Row(
                [
                    ft.Icon(icon, size=40, color=color),
                    ft.Column(
                        [
                            ft.Text(name, weight="bold", size=14),
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

    def render(self):
        return ft.Column(
            controls=[
                ft.Container(
                    content=self.main_content,
                    expand=True,
                ),
                self.bottom_nav,
            ],
            expand=True,
            spacing=0,
        )
