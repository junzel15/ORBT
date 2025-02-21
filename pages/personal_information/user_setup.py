import flet as ft


class UserSetupPage(ft.UserControl):
    def __init__(self, page: ft.Page, go_to):
        super().__init__()
        self.page = page
        self.go_to = go_to

        self.page.title = "User-Setup"
        self.page.padding = 0
        self.page.scroll = "adaptive"
        self.page.bgcolor = "#000000"

        self.page.window_width = 400
        self.page.window_height = 730
        self.page.update()

        self.image = ft.Image(
            src="images/user_setup.png",
            width=271,
            height=203,
            fit="contain",
        )

        self.title_text = ft.Text(
            "Tell us a bit about yourself",
            size=52,
            font_family="Sora-SemiBold",
            color="white",
            text_align="left",
        )

        self.description_text = ft.Text(
            "Help us get to know you better and personalize your ORBT experience. This should only take a few minutes, and you can skip any part if you'd like.",
            size=13,
            font_family="InstrumentSans-Regular",
            color="white",
            text_align="left",
        )

        self.continue_button = ft.ElevatedButton(
            text="Continue",
            on_click=lambda e: self.go_to("/gender", self.page),
            bgcolor="#7C4DFF",
            color="white",
            width=300,
            height=50,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                text_style=ft.TextStyle(
                    font_family="InstrumentSans-SemiBold",
                    size=16,
                ),
            ),
        )

    def render(self):
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=self.image,
                                alignment=ft.alignment.center,
                                padding=ft.padding.only(top=50, bottom=20),
                            ),
                            ft.Container(
                                content=self.title_text,
                                alignment=ft.alignment.top_left,
                                padding=ft.padding.only(bottom=16, left=16),
                            ),
                            ft.Container(
                                content=self.description_text,
                                alignment=ft.alignment.top_left,
                                padding=ft.padding.only(bottom=50, left=16),
                            ),
                        ],
                        alignment="start",
                        spacing=0,
                    ),
                    expand=True,
                    padding=ft.padding.all(16),
                    alignment=ft.alignment.center,
                    bgcolor="#000000",
                ),
                ft.Container(
                    content=self.continue_button,
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(bottom=20),
                    bgcolor="#000000",
                ),
            ],
            expand=True,
            spacing=0,
        )
