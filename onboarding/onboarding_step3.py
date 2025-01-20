import flet as ft


def OnboardingStep3(page, go_to):
    def get_started(e):

        page.go("/registration")

    return ft.View(
        "/onboarding3",
        controls=[
            ft.Container(
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_left,
                    colors=["black", "#5300FA"],
                    stops=[
                        0.1,
                        1.0,
                    ],
                ),
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
                            padding=ft.padding.only(top=20),
                        ),
                        ft.Container(
                            content=ft.Image(
                                src="assets/images/Onboarding 3 Graphics.png",
                                fit=ft.ImageFit.CONTAIN,
                                height=320,
                            ),
                            alignment=ft.alignment.center,
                            padding=ft.padding.symmetric(vertical=20),
                        ),
                        ft.Container(
                            content=ft.Text(
                                "Build the Lasting Connections",
                                size=28,
                                weight="bold",
                                text_align=ft.TextAlign.CENTER,
                                color="white",
                            ),
                            alignment=ft.alignment.center,
                            padding=ft.padding.only(top=0),
                        ),
                        ft.Container(
                            content=ft.Text(
                                "Forge meaningful connections that grow your community and enrich your life beyond every event.",
                                size=16,
                                text_align=ft.TextAlign.CENTER,
                                color="white70",
                            ),
                            alignment=ft.alignment.center,
                            padding=ft.padding.symmetric(horizontal=40, vertical=0),
                        ),
                        ft.Container(
                            content=ft.ElevatedButton(
                                "Get Started",
                                on_click=get_started,
                                style=ft.ButtonStyle(
                                    color="5300FA",
                                    bgcolor="white",
                                    shape=ft.RoundedRectangleBorder(radius=20),
                                    padding=ft.padding.symmetric(
                                        horizontal=80, vertical=15
                                    ),
                                    text_style=ft.TextStyle(
                                        size=22, weight="bold", color="5300FA"
                                    ),
                                ),
                            ),
                            alignment=ft.alignment.center,
                            expand=True,
                            padding=ft.padding.symmetric(vertical=10),
                        ),
                        ft.Container(
                            content=ft.TextButton(
                                "Already have an account? Log in",
                                on_click=get_started,
                                style=ft.ButtonStyle(
                                    color="white",
                                    padding=ft.padding.all(0),
                                ),
                            ),
                            alignment=ft.alignment.center,
                            padding=ft.padding.symmetric(vertical=0),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=0,
                    expand=True,
                ),
            ),
        ],
    )
