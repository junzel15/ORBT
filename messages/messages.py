import flet as ft


class MessagesPage(ft.UserControl):
    def __init__(self, page: ft.Page, go_to):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.route = "/messages"

        self.page.title = "Messages"
        self.page.padding = 0
        self.page.bgcolor = "#F8F9FA"

        self.main_content = self.build_main_content()
        self.bottom_nav = self.build_bottom_nav()

    def build_main_content(self):
        def message_item(icon, name, message, time, color="white"):
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

        search_bar = ft.TextField(
            hint_text="Search",
            prefix_icon=ft.icons.SEARCH,
            expand=True,
            border_radius=5,
        )

        filter_buttons = ft.Row(
            [
                ft.ElevatedButton("All", expand=True, color="white", bgcolor="#6200EE"),
                ft.ElevatedButton("Direct", expand=True, color="black"),
                ft.ElevatedButton("Group Chat", expand=True, color="black"),
            ],
            alignment="spaceEvenly",
        )

        messages_list = [
            message_item(
                ft.icons.EVENT,
                "Event: BRO001",
                "ORB: The countdown is over - Let the...",
                "Exp: 4hrs",
                color="#6200EE",
            ),
            message_item(
                ft.icons.EVENT,
                "Event: BAO001",
                "Inka: On my way guys, See you!",
                "Exp: 4hrs",
                color="#6200EE",
            ),
            message_item(
                ft.icons.FAVORITE,
                "Event: EXO001",
                "You: See you!",
                "Exp: 4hrs",
                color="#6200EE",
            ),
        ]

        return ft.ListView(
            controls=[
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.ARROW_BACK,
                            on_click=lambda e: self.go_to("/booking"),
                        ),
                        ft.Text("Messages", size=20, weight="bold"),
                    ],
                    alignment="start",
                    spacing=10,
                ),
                ft.Divider(height=10, thickness=1),
                search_bar,
                ft.Divider(height=10, thickness=1),
                filter_buttons,
                ft.Divider(height=10, thickness=1),
                *messages_list,
            ],
            spacing=10,
            expand=True,
            padding=ft.padding.all(16),
        )

    def build_bottom_nav(self):
        is_mobile = self.page.window_width < 600

        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        content=ft.Image(
                            src="assets/images/Home.png",
                            width=(24 if not is_mobile else 20),
                            height=(24 if not is_mobile else 20),
                        ),
                        icon_size=24,
                        icon_color="#000000",
                        on_click=lambda _: self.go_to("/booking"),
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src="assets/images/Star.png",
                            width=(24 if not is_mobile else 20),
                            height=(24 if not is_mobile else 20),
                        ),
                        icon_size=24,
                        icon_color="#000000",
                        on_click=lambda _: self.go_to("/bookings/upcoming"),
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src="assets/images/Message.png",
                            width=(24 if not is_mobile else 20),
                            height=(24 if not is_mobile else 20),
                        ),
                        icon_size=24,
                        icon_color="#000000",
                        on_click=lambda e: self.go_to("/messages"),
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src="assets/images/Profile.png",
                            width=(24 if not is_mobile else 20),
                            height=(24 if not is_mobile else 20),
                        ),
                        icon_size=24,
                        icon_color="#000000",
                        on_click=lambda e: self.go_to("/profile"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            bgcolor="#FFFFFF",
            padding=ft.padding.symmetric(vertical=10),
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
