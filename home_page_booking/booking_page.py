import flet as ft


class BookingPage:
    def __init__(self, page: ft.Page, go_to):
        self.page = page
        self.go_to = go_to

    def render(self):
        return ft.View(
            route="/booking",
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Image(
                                        src="assets/images/Location.png",
                                        width=32,
                                        height=32,
                                    ),
                                    ft.Text(
                                        "Add your location",
                                        size=14,
                                        style="Instrument Sans",
                                        color="#747688",
                                        expand=1,
                                    ),
                                ],
                                spacing=8,
                            ),
                            ft.Image(
                                src="assets/images/Notify.png",
                                width=24,
                                height=24,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    padding=ft.padding.symmetric(horizontal=16),
                    margin=ft.margin.only(bottom=16),
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Text(
                                        "Hello, ",
                                        size=32,
                                        weight="bold",
                                        color="#000000",
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    ft.Text(
                                        "John!",
                                        size=32,
                                        weight="bold",
                                        color="#6D28D9",
                                        text_align=ft.TextAlign.CENTER,
                                        style="underline",
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Text(
                                "Find your crowd",
                                size=24,
                                weight="bold",
                                text_align=ft.TextAlign.CENTER,
                                color="#000000",
                            ),
                            ft.Text(
                                "Share the moment",
                                size=24,
                                weight="bold",
                                text_align=ft.TextAlign.CENTER,
                                color="#3F4CCF",
                            ),
                            ft.Text(
                                "Book now, meet 5 strangers,\nand let the fun find you.",
                                size=16,
                                text_align=ft.TextAlign.CENTER,
                                color="#4B4B4B",
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,
                    padding=ft.padding.symmetric(horizontal=16),
                ),
                ft.Container(
                    content=ft.Image(
                        src="assets/images/Homepage Graphics.png",
                        width=350,
                        height=150,
                        fit=ft.ImageFit.COVER,
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.symmetric(vertical=16),
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Image(
                                            src="assets/images/Icon Dinning.png",
                                            width=50,
                                            height=30,
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                        ft.Text(
                                            "Dining",
                                            size=20,
                                            weight="bold",
                                            color="white",
                                            expand=1,
                                        ),
                                        ft.Icon(
                                            ft.icons.ARROW_FORWARD,
                                            color="white",
                                            size=24,
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                                padding=ft.padding.all(16),
                                border_radius=12,
                                on_click=lambda e: self.go_to("/dining/coffee"),
                            ),
                            ft.Divider(height=1, color="#FFFFFF22"),
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Image(
                                            src="assets/images/Icon Bars.png",
                                            width=50,
                                            height=30,
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                        ft.Text(
                                            "Bars",
                                            size=20,
                                            weight="bold",
                                            color="white",
                                            expand=1,
                                        ),
                                        ft.Icon(
                                            ft.icons.ARROW_FORWARD,
                                            color="white",
                                            size=24,
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                                padding=ft.padding.all(16),
                                border_radius=12,
                                on_click=lambda e: self.go_to("/bars"),
                            ),
                            ft.Divider(height=1, color="#FFFFFF22"),
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Image(
                                            src="assets/images/Icon Experiences.png",
                                            width=50,
                                            height=30,
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                        ft.Text(
                                            "Experiences",
                                            size=20,
                                            weight="bold",
                                            color="white",
                                            expand=1,
                                        ),
                                        ft.Icon(
                                            ft.icons.ARROW_FORWARD,
                                            color="white",
                                            size=24,
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                                padding=ft.padding.all(16),
                                border_radius=12,
                                on_click=lambda e: self.go_to("/experience"),
                            ),
                        ],
                        spacing=0,
                    ),
                    padding=ft.padding.symmetric(horizontal=16),
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=["#1a1a1a", "#5300FA"],
                    ),
                    border_radius=12,
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.HOME,
                                icon_size=24,
                                icon_color="#000000",
                            ),
                            ft.IconButton(
                                icon=ft.icons.CALENDAR_TODAY,
                                icon_size=24,
                                icon_color="#000000",
                            ),
                            ft.IconButton(
                                icon=ft.icons.CHAT_BUBBLE_OUTLINE,
                                icon_size=24,
                                icon_color="#000000",
                            ),
                            ft.IconButton(
                                icon=ft.icons.PERSON,
                                icon_size=24,
                                icon_color="#000000",
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    ),
                    padding=ft.padding.symmetric(vertical=12, horizontal=8),
                    bgcolor="#FFFFFF",
                    border_radius=ft.border_radius.all(24),
                    shadow=ft.BoxShadow(
                        spread_radius=4,
                        blur_radius=8,
                        color="#00000022",
                        offset=ft.Offset(0, 2),
                    ),
                    margin=ft.margin.all(16),
                ),
            ],
            padding=ft.padding.all(0),
        )
