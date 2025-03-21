import flet as ft


class OnboardingStep1(ft.View):
    def __init__(self, page, go_to):
        super().__init__(
            route="/onboarding1",
            controls=[
                ft.Container(
                    bgcolor="black",
                    expand=True,
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Image(
                                    src="images/logo.png",
                                    width=103,
                                    height=30,
                                ),
                                alignment=ft.alignment.top_center,
                                padding=ft.padding.only(top=40),
                            ),
                            ft.Container(
                                content=ft.Image(
                                    src="images/orbit_people.png",
                                    width=302,
                                    height=314,
                                ),
                                alignment=ft.alignment.center,
                                padding=ft.padding.symmetric(vertical=20),
                            ),
                            ft.Container(
                                content=ft.Text(
                                    "Discover Your ORBT",
                                    font_family="Sora-SemiBold",
                                    size=28,
                                    weight="bold",
                                    text_align=ft.TextAlign.CENTER,
                                    color="white",
                                ),
                                alignment=ft.alignment.center,
                                padding=ft.padding.only(bottom=10),
                            ),
                            ft.Container(
                                content=ft.Text(
                                    "Connect with a curated group of individuals who share your interests for an engaging experience.",
                                    font_family="InstrumentSans-Regular",
                                    size=14,
                                    text_align=ft.TextAlign.CENTER,
                                    color="white70",
                                ),
                                alignment=ft.alignment.center,
                                padding=ft.padding.symmetric(horizontal=30),
                            ),
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.TextButton(
                                            "Skip",
                                            on_click=lambda _: page.go("/onboarding3"),
                                            style=ft.ButtonStyle(
                                                text_style=ft.TextStyle(
                                                    font_family="InstrumentSans-Regular",
                                                    size=16,
                                                    color="white70",
                                                )
                                            ),
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Image(
                                                    src="images/progress_rectangle.png",
                                                    width=20,
                                                    height=10,
                                                ),
                                                ft.Image(
                                                    src="images/progress_dot.png",
                                                    width=10,
                                                    height=10,
                                                ),
                                                ft.Image(
                                                    src="images/progress_dot.png",
                                                    width=10,
                                                    height=10,
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                        ),
                                        ft.TextButton(
                                            "Next",
                                            on_click=lambda _: page.go("/onboarding2"),
                                            style=ft.ButtonStyle(
                                                text_style=ft.TextStyle(
                                                    font_family="InstrumentSans-Regular",
                                                    size=16,
                                                    color="white",
                                                )
                                            ),
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                                padding=ft.padding.symmetric(
                                    horizontal=20, vertical=10
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        expand=True,
                    ),
                ),
            ],
        )

        self.page = page
        self.go_to = go_to

        self.page.window_width = 400
        self.page.window_height = 680
        self.page.update()
