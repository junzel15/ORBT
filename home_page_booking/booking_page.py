import flet as ft


class BookingPage:
    def __init__(self, page: ft.Page, go_to):
        self.page = page
        self.go_to = go_to

    def render(self):
        is_mobile = self.page.window_width < 600

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
                                        width=(32 if not is_mobile else 24),
                                        height=32 if not is_mobile else 24,
                                    ),
                                    ft.Text(
                                        "Add your location",
                                        size=(14 if not is_mobile else 12),
                                        style="Instrument Sans",
                                        color="#747688",
                                        expand=1,
                                    ),
                                ],
                                spacing=8,
                            ),
                            ft.Image(
                                src="assets/images/Notify.png",
                                width=24 if not is_mobile else 20,
                                height=24 if not is_mobile else 20,
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
                                        size=16 if not is_mobile else 14,
                                        style="Instrument Sans",
                                        color="#000000",
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    ft.Text(
                                        "John!",
                                        size=16 if not is_mobile else 14,
                                        style="Instrument Sans",
                                        color="#6D28D9",
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Text(
                                "Find your crowd",
                                size=26 if not is_mobile else 20,
                                style="Instrument Sans",
                                color="#000000",
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Text(
                                "Share the moment",
                                size=26 if not is_mobile else 20,
                                style="Sora",
                                color=ft.LinearGradient(
                                    begin=ft.alignment.top_center,
                                    end=ft.alignment.bottom_center,
                                    colors=["#8547FF", "#000000"],
                                ),
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Text(
                                "Book now, meet 5 strangers,\nand let the fun find you.",
                                size=16 if not is_mobile else 14,
                                style="Instrument Sans",
                                color="#4B4B4B",
                                text_align=ft.TextAlign.CENTER,
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
                        width=(350 if not is_mobile else 250),
                        height=150 if not is_mobile else 120,
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
                                            width=(50 if not is_mobile else 40),
                                            height=30 if not is_mobile else 24,
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                        ft.Text(
                                            "Dining",
                                            expand=1,
                                            size=(24 if not is_mobile else 18),
                                            style="Sora",
                                            color="#FFFFFF",
                                        ),
                                        ft.Icon(
                                            ft.icons.ARROW_FORWARD,
                                            color="white",
                                            size=(24 if not is_mobile else 20),
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
                                            width=50 if not is_mobile else 40,
                                            height=30 if not is_mobile else 24,
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                        ft.Text(
                                            "Bars",
                                            size=24 if not is_mobile else 18,
                                            style="Sora",
                                            color="#FFFFFF",
                                            expand=1,
                                        ),
                                        ft.Icon(
                                            ft.icons.ARROW_FORWARD,
                                            color="white",
                                            size=24 if not is_mobile else 20,
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
                                            width=50 if not is_mobile else 40,
                                            height=30 if not is_mobile else 24,
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                        ft.Text(
                                            "Experiences",
                                            size=24 if not is_mobile else 18,
                                            style="Sora",
                                            color="#FFFFFF",
                                            expand=1,
                                        ),
                                        ft.Icon(
                                            ft.icons.ARROW_FORWARD,
                                            color="white",
                                            size=24 if not is_mobile else 20,
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
                        scroll="always",
                    ),
                    padding=ft.padding.symmetric(horizontal=16),
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=["#1a1a1a", "#5300FA"],
                    ),
                    border_radius=12,
                    expand=True,
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.IconButton(
                                    content=ft.Image(
                                        src="assets/images/Home.png",
                                        width=(24 if not is_mobile else 20),
                                        height=24 if not is_mobile else 20,
                                    ),
                                    icon_size=24,
                                    icon_color="#000000",
                                ),
                            ),
                            ft.Container(
                                content=ft.IconButton(
                                    content=ft.Image(
                                        src="assets/images/Star.png",
                                        width=(24 if not is_mobile else 20),
                                        height=24 if not is_mobile else 20,
                                    ),
                                    icon_size=24,
                                    icon_color="#000000",
                                ),
                            ),
                            ft.Container(
                                content=ft.IconButton(
                                    content=ft.Image(
                                        src="assets/images/Message.png",
                                        width=(24 if not is_mobile else 20),
                                        height=24 if not is_mobile else 20,
                                    ),
                                    icon_size=24,
                                    icon_color="#000000",
                                    on_click=lambda e: self.go_to("/messages"),
                                ),
                            ),
                            ft.Container(
                                content=ft.IconButton(
                                    content=ft.Image(
                                        src="assets/images/Profile.png",
                                        width=(24 if not is_mobile else 20),
                                        height=24 if not is_mobile else 20,
                                    ),
                                    icon_size=24,
                                    icon_color="#000000",
                                    on_click=lambda e: self.go_to("/profile"),
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    ),
                    bgcolor="#FFFFFF",
                    border_radius=30,
                ),
            ],
            padding=ft.padding.all(0),
            scroll="always",
        )
