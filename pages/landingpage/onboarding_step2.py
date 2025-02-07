import flet as ft


class OnboardingStep2(ft.View):
    def __init__(self, page, go_to):
        super().__init__(
            route="/onboarding2",
            controls=[
                ft.Container(
                    bgcolor="black",
                    expand=True,
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Image(
                                    src="assets/images/ORBT Logo - Splash Screen.png",
                                    fit=ft.ImageFit.CONTAIN,
                                    height=30,
                                ),
                                alignment=ft.alignment.top_center,
                                padding=ft.padding.only(top=40),
                            ),
                            ft.Container(
                                content=ft.Image(
                                    src="assets/images/Onboarding 2 Graphics.png",
                                    fit=ft.ImageFit.CONTAIN,
                                    height=300,
                                ),
                                alignment=ft.alignment.center,
                                padding=ft.padding.symmetric(vertical=20),
                            ),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text(
                                            "Curate Your Experience",
                                            font_family="Sora-SemiBold",
                                            size=28,
                                            weight="bold",
                                            text_align=ft.TextAlign.CENTER,
                                            color="white",
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                alignment=ft.alignment.center,
                                expand=True,
                            ),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text(
                                            "Choose exclusive dinners and events that match your schedule and preferences.",
                                            font_family="InstrumentSans-Regular",
                                            size=14,
                                            text_align=ft.TextAlign.CENTER,
                                            color="white70",
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                alignment=ft.alignment.center,
                                expand=True,
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
                                                    src="images/progress_dot.png",
                                                    width=10,
                                                    height=10,
                                                ),
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
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                        ),
                                        ft.TextButton(
                                            "Next",
                                            on_click=lambda _: page.go("/onboarding3"),
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
                        alignment=ft.MainAxisAlignment.CENTER,
                        expand=True,
                    ),
                ),
            ],
        )
