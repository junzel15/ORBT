import flet as ft


def OnboardingStep1(page, go_to):
    def next_step(e):
        page.go("/onboarding2")

    return ft.View(
        "/onboarding1",
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
                                src="assets/images/Onboarding 1 Graphics.png",
                                fit=ft.ImageFit.CONTAIN,
                                height=300,
                            ),
                            alignment=ft.alignment.center,
                            padding=ft.padding.symmetric(vertical=20),
                        ),
                        ft.Container(
                            content=ft.Container(
                                content=ft.Text(
                                    "Discover Your ORBT",
                                    size=28,
                                    weight="bold",
                                    text_align=ft.TextAlign.CENTER,
                                    color="white",
                                ),
                                alignment=ft.alignment.center,
                                padding=ft.padding.only(bottom=10),
                            ),
                        ),
                        ft.Container(
                            content=ft.Text(
                                "Connect with a curated group of individuals who share your interests for an engaging experience.",
                                size=16,
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
                                        style=ft.ButtonStyle(color="white70"),
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Container(
                                                width=8,
                                                height=8,
                                                bgcolor="white",
                                                border_radius=8,
                                            ),
                                            ft.Container(
                                                width=8,
                                                height=8,
                                                bgcolor="white70",
                                                border_radius=8,
                                                margin=ft.margin.symmetric(
                                                    horizontal=4
                                                ),
                                            ),
                                            ft.Container(
                                                width=8,
                                                height=8,
                                                bgcolor="white70",
                                                border_radius=8,
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    ft.TextButton(
                                        "Next",
                                        on_click=next_step,
                                        style=ft.ButtonStyle(color="white"),
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            padding=ft.padding.symmetric(horizontal=20, vertical=10),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    expand=True,
                ),
            ),
        ],
    )
