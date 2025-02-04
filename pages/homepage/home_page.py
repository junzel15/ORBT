import flet as ft
from global_state import get_logged_in_user


class HomePage:

    def __init__(self, page: ft.Page, go_to, user):
        self.page = page
        self.go_to = go_to
        self.user = get_logged_in_user()
        self.user_name = self.user.get("full_name", "Guest") if self.user else "Guest"

    def render(self):
        self.user = get_logged_in_user()
        self.user_name = self.user.get("full_name", "Guest") if self.user else "Guest"
        is_mobile = self.page.window_width < 600

        self.Notification_Section = ft.Container(
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
        )

        self.Greeting_Description_Section = ft.Container(
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
                                self.user_name,
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
        )

        self.Image_Section = ft.Container(
            content=ft.Image(
                src="assets/images/Homepage Graphics.png",
                width=(350 if not is_mobile else 250),
                height=150 if not is_mobile else 120,
                fit=ft.ImageFit.COVER,
            ),
            alignment=ft.alignment.center,
            margin=ft.margin.symmetric(vertical=16),
        )

        self.Options_Section = ft.Container(
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
                        on_click=lambda e: self.go_to("/coffee", self.page),
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
                        on_click=lambda e: self.go_to("/bars", self.page),
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
                        on_click=lambda e: self.go_to("/experience", self.page),
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
        )

        self.bottom_nav = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.IconButton(
                            content=ft.Image(
                                src="assets/images/Home.png",
                                width=24,
                                height=24,
                            ),
                            icon_size=24,
                            icon_color="#000000",
                            on_click=lambda _: self.go_to("/home", self.page),
                        ),
                    ),
                    ft.Container(
                        content=ft.IconButton(
                            content=ft.Image(
                                src="assets/images/Star.png",
                                width=24,
                                height=24,
                            ),
                            icon_size=24,
                            icon_color="#000000",
                            on_click=lambda _: self.go_to("/upcoming", self.page),
                        ),
                    ),
                    ft.Container(
                        content=ft.IconButton(
                            content=ft.Image(
                                src="assets/images/Message.png",
                                width=24,
                                height=24,
                            ),
                            icon_size=24,
                            icon_color="#000000",
                            on_click=lambda _: self.go_to("/messages", self.page),
                        ),
                    ),
                    ft.Container(
                        content=ft.IconButton(
                            content=ft.Image(
                                src="assets/images/Profile.png",
                                width=24,
                                height=24,
                            ),
                            icon_size=24,
                            icon_color="#000000",
                            on_click=lambda _: self.go_to("/profile", self.page),
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            bgcolor="#FFFFFF",
            border_radius=30,
            padding=ft.padding.symmetric(vertical=10),
        )

        self.main_content = ft.ListView(
            controls=[
                self.Notification_Section,
                self.Greeting_Description_Section,
                self.Image_Section,
                self.Options_Section,
            ],
            expand=True,
        )

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
