import flet as ft
from flet import UserControl


class CancelSuccessful(ft.UserControl):
    def __init__(self, page, go_to):
        self.go_to = go_to
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(height=40),
                    ft.Image(
                        src="images/calendar.png",
                        width=220,
                        height=280,
                    ),
                    ft.Container(height=25),
                    ft.Text(
                        "Your Booking Has Been Cancelled",
                        font_family="Sora-Bold",
                        size=26,
                        text_align=ft.TextAlign.CENTER,
                        width=320,
                        color="#FFFFFF",
                    ),
                    ft.Container(height=15),
                    ft.Text(
                        "We’re sorry to see you go, but we hope to see you again soon! "
                        "If there’s anything we can do to improve your experience, let us know.",
                        font_family="InstrumentSans-Regular",
                        size=14,
                        text_align=ft.TextAlign.CENTER,
                        width=320,
                        color="#FFFFFF",
                    ),
                    ft.Container(height=40),
                    ft.ElevatedButton(
                        width=300,
                        height=55,
                        content=ft.Text(
                            value="Back to Home",
                            font_family="InstrumentSans-SemiBold",
                            size=16,
                            color="#FFFFFF",
                        ),
                        bgcolor="#5300FA",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=12),
                        ),
                        on_click=self.on_get_started_click,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            alignment=ft.alignment.top_center,
            image_src="assets/images/Dark Background 2 Screen.png",
            image_fit=ft.ImageFit.COVER,
            padding=ft.Padding(30, 20, 30, 30),
        )

    def on_get_started_click(self, _):
        self.page.go("/homepage")
