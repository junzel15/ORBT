import flet as ft


def OnboardingStep2(page, go_to):
    def next_step(e):
        page.go("/onboarding3")

    def previous_step(e):
        page.go("/onboarding1")

    return ft.View(
        "/onboarding2",
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
                                        size=16,
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
                                        "Back",
                                        on_click=previous_step,
                                        style=ft.ButtonStyle(color="white70"),
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Container(
                                                width=8,
                                                height=8,
                                                bgcolor="white70",
                                                border_radius=8,
                                            ),
                                            ft.Container(
                                                width=8,
                                                height=8,
                                                bgcolor="white",
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
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,
                ),
            ),
        ],
    )
