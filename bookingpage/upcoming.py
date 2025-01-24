import flet as ft


class UpcomingPage:
    def __init__(self, page: ft.Page, go_to):
        self.page = page
        self.go_to = go_to

        self.page.title = "Upcoming"
        self.page.padding = 0
        self.page.scroll = "adaptive"
        self.page.bgcolor = "#000000"
        self.build()

        self.page.add(self.render())

    def build(self):
        self.header = ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.IconButton(
                                icon=ft.icons.ARROW_BACK,
                                icon_size=20,
                                icon_color="#FFFFFF",
                                on_click=lambda _: self.go_to("/homepage", self.page),
                            ),
                            ft.Text(
                                "My Bookings", size=18, color="#FFFFFF", weight="bold"
                            ),
                            ft.IconButton(
                                icon=ft.icons.TUNE,
                                icon_size=20,
                                icon_color="#FFFFFF",
                            ),
                        ],
                        alignment="spaceBetween",
                    ),
                    ft.Container(
                        content=ft.TextField(
                            hint_text="Search Events, Dates, Places ...",
                            hint_style=ft.TextStyle(size=14, color="#A4A4A4"),
                            text_size=14,
                            border_radius=30,
                            filled=True,
                            fill_color="#1A1A1A",
                            border_color="transparent",
                            content_padding=ft.padding.symmetric(
                                horizontal=16, vertical=12
                            ),
                            prefix_icon=ft.Icon(ft.icons.SEARCH, color="#A4A4A4"),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.TextButton(
                                    text="Upcoming",
                                    style=ft.ButtonStyle(
                                        text_style=ft.TextStyle(
                                            size=14,
                                            weight="bold",
                                            color="#5300FA",
                                        ),
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                        bgcolor="#FFFFFF",
                                        padding=ft.padding.symmetric(
                                            horizontal=16, vertical=8
                                        ),
                                    ),
                                    on_click=lambda _: self.go_to(
                                        "/bookings/upcoming", self.page
                                    ),
                                ),
                                ft.TextButton(
                                    text="Completed",
                                    style=ft.ButtonStyle(
                                        text_style=ft.TextStyle(
                                            size=14,
                                            weight="bold",
                                            color="#FFFFFF",
                                        ),
                                        padding=ft.padding.symmetric(
                                            horizontal=16, vertical=8
                                        ),
                                    ),
                                    on_click=lambda _: self.go_to(
                                        "/bookings/completed", self.page
                                    ),
                                ),
                                ft.TextButton(
                                    text="Cancelled",
                                    style=ft.ButtonStyle(
                                        text_style=ft.TextStyle(
                                            size=14,
                                            weight="bold",
                                            color="#FFFFFF",
                                        ),
                                        padding=ft.padding.symmetric(
                                            horizontal=16, vertical=8
                                        ),
                                    ),
                                    on_click=lambda _: self.go_to(
                                        "/bookings/cancelled", self.page
                                    ),
                                ),
                            ],
                            alignment="start",
                            spacing=20,
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ],
                spacing=12,
            ),
            padding=ft.padding.all(16),
            height=210,
            width=210,
            bgcolor=None,
            image_src="assets/images/Rectangle.png",
            image_fit="cover",
        )

        self.subfilters = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text("This week", color="#FFFFFF", size=12),
                        padding=ft.padding.symmetric(horizontal=10, vertical=5),
                        bgcolor="#000000",
                        border_radius=20,
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                    ft.Container(
                        content=ft.Text("Next Week", color="#000000", size=12),
                        padding=ft.padding.symmetric(horizontal=10, vertical=5),
                        bgcolor="#FFFFFF",
                        border_radius=20,
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                    ft.Container(
                        content=ft.Text("Later", color="#000000", size=12),
                        padding=ft.padding.symmetric(horizontal=10, vertical=5),
                        bgcolor="#FFFFFF",
                        border_radius=20,
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                ],
                alignment="spaceAround",
                spacing=10,
            ),
            margin=ft.margin.symmetric(vertical=10),
        )

        def booking_card(title, subtitle, date_time, location, tag_color):
            return ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Icon(
                                    ft.icons.RESTAURANT_MENU, size=20, color=tag_color
                                ),
                                ft.Text(title, size=16, weight="bold", color="#000000"),
                                ft.Container(
                                    content=ft.Text(subtitle, size=10, color="#000000"),
                                    padding=ft.padding.symmetric(
                                        horizontal=5, vertical=2
                                    ),
                                    bgcolor="#FFFFFF",
                                    border_radius=10,
                                ),
                            ],
                            alignment="spaceBetween",
                        ),
                        ft.Text(f"DATE & TIME\n{date_time}", size=12, color="#000000"),
                        ft.Text(f"LOCATION\n{location}", size=12, color="#000000"),
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Cancel",
                                    color="#000000",
                                    bgcolor="#FFFFFF",
                                ),
                                ft.ElevatedButton(
                                    "View Details",
                                    color="#FFFFFF",
                                    bgcolor="#0000FF",
                                ),
                            ],
                            alignment="spaceBetween",
                        ),
                    ],
                    spacing=5,
                ),
                padding=ft.padding.all(10),
                border_radius=10,
                bgcolor="#E0E0E0",
                margin=ft.margin.symmetric(vertical=5),
            )

        self.bookings = ft.Column(
            controls=[
                booking_card(
                    "No data",
                    "",
                    "No data",
                    "No data",
                    "No data",
                ),
            ],
        )

        is_mobile = self.page.window_width < 600
        self.bottom_nav = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.IconButton(
                            content=ft.Image(
                                src="assets/images/Home.png",
                                width=(24 if not is_mobile else 20),
                                height=(24 if not is_mobile else 20),
                            ),
                            icon_size=24,
                            icon_color="#000000",
                            on_click=lambda _: self.go_to("/homepage", self.page),
                        ),
                    ),
                    ft.Container(
                        content=ft.IconButton(
                            content=ft.Image(
                                src="assets/images/Star.png",
                                width=(24 if not is_mobile else 20),
                                height=(24 if not is_mobile else 20),
                            ),
                            icon_size=24,
                            icon_color="#000000",
                            on_click=lambda _: self.go_to(
                                "/bookings/upcoming", self.page
                            ),
                        ),
                    ),
                    ft.Container(
                        content=ft.IconButton(
                            content=ft.Image(
                                src="assets/images/Message.png",
                                width=(24 if not is_mobile else 20),
                                height=(24 if not is_mobile else 20),
                            ),
                            icon_size=24,
                            icon_color="#000000",
                            on_click=lambda e: self.go_to("/messages", self.page),
                        ),
                    ),
                    ft.Container(
                        content=ft.IconButton(
                            content=ft.Image(
                                src="assets/images/Profile.png",
                                width=(24 if not is_mobile else 20),
                                height=(24 if not is_mobile else 20),
                            ),
                            icon_size=24,
                            icon_color="#000000",
                            on_click=lambda e: self.go_to("/profile", self.page),
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
                self.header,
                self.subfilters,
                self.bookings,
            ],
            expand=True,
            padding=ft.padding.all(10),
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
