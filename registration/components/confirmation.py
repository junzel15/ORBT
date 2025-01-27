import flet as ft


class ConfirmationPage(ft.UserControl):

    def __init__(self, page, go_to):
        self.go_to = go_to
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(height=40),
                    ft.Container(
                        content=ft.Text(
                            "You're all set!",
                            font_family="Sora-SemiBold",
                            size=20,
                            text_align=ft.TextAlign.CENTER,
                            width=240,
                        ),
                    ),
                    ft.Container(
                        content=ft.Text(
                            "Your account has been successfully verified. Let's get to know you better!",
                            font_family="InstrumentSans-Regular",
                            size=14,
                            text_align=ft.TextAlign.CENTER,
                            width=240,
                        ),
                    ),
                    ft.Container(height=20),
                    ft.Container(
                        content=ft.Image(
                            src="images/all_set_mid.png", width=255, height=321
                        ),
                        alignment=ft.alignment.top_center,
                        padding=ft.Padding(0, 0, 0, 0),
                    ),
                    ft.Container(height=120),
                    ft.Container(
                        padding=ft.Padding(20, 0, 0, 0),
                        content=ft.ElevatedButton(
                            width=1000,
                            height=50,
                            content=ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text(
                                            value="Get Started",
                                            font_family="InstrumentSans-SemiBold",
                                            size=16,
                                            color="#FFFFFF",
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                padding=ft.padding.all(10),
                            ),
                            bgcolor="#5300FA",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                            ),
                            on_click=self.on_get_started_click,
                        ),
                    ),
                    ft.Container(height=10),
                    ft.Container(height=1000),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            alignment=ft.alignment.top_center,
            bgcolor=ft.Colors.WHITE,
            padding=ft.Padding(20, 0, 20, 10),
        )

    def on_get_started_click(self, _):
        print("Back Click")
        if self.on_get_started:
            self.on_get_started()
