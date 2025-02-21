import flet as ft


class OnboardingStep3(ft.UserControl):
    def __init__(self, page, go_to):
        super().__init__()
        self.page = page
        self.go_to = go_to

        self.page.window_width = 400
        self.page.window_height = 700
        self.page.update()

    def get_started(self, e):
        self.page.go("/registration")

    def build(self):
        return ft.Container(
            content=ft.Stack(
                controls=[
                    ft.Image(
                        src="images/onboarding_bg.png",
                        fit=ft.ImageFit.CONTAIN,
                        expand=True,
                    ),
                    ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Image(
                                    src="images/ORBT Logo - Splash Screen.png",
                                    fit=ft.ImageFit.CONTAIN,
                                    height=30,
                                ),
                                alignment=ft.alignment.top_center,
                                padding=ft.padding.only(top=40),
                            ),
                            ft.Container(
                                content=ft.Image(
                                    src="images/Onboarding 3 Graphics.png",
                                    fit=ft.ImageFit.CONTAIN,
                                    height=320,
                                ),
                                alignment=ft.alignment.center,
                                padding=ft.padding.symmetric(vertical=20),
                            ),
                            ft.Container(
                                content=ft.Text(
                                    "Build the Lasting Connections",
                                    font_family="Sora-SemiBold",
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
                                    font_family="InstrumentSans-Regular",
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
                                    on_click=self.get_started,
                                    style=ft.ButtonStyle(
                                        color="5300FA",
                                        bgcolor="white",
                                        shape=ft.RoundedRectangleBorder(radius=20),
                                        padding=ft.padding.symmetric(
                                            horizontal=80, vertical=15
                                        ),
                                        text_style=ft.TextStyle(
                                            font_family="InstrumentSans-SemiBold",
                                            size=22,
                                            weight="bold",
                                            color="5300FA",
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
                                    on_click=self.get_started,
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
                ]
            )
        )
