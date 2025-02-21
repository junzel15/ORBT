import flet as ft
from flet import UserControl


class CancelSuccessful(ft.UserControl):
    def __init__(self, page, go_to):
        self.go_to = go_to
        super().__init__()
        self.page = page

        self.page.window_width = 375
        self.page.window_height = 667
        self.page.update()

    def adjust_window_size(self):
        screen_width = self.page.window_width
        screen_height = self.page.window_height
        if screen_width <= 480:
            self.page.window_width = screen_width
            self.page.window_height = screen_height
        elif 481 <= screen_width <= 1024:
            self.page.window_width = min(screen_width, 800)
            self.page.window_height = min(screen_height, 1000)
        else:
            self.page.window_width = min(screen_width, 1200)
            self.page.window_height = min(screen_height, 900)
        self.page.update()

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(height=20),
                    ft.Image(
                        src="images/calendar.png",
                        width=self.page.window_width * 0.6,
                        height=self.page.window_width * 0.75,
                    ),
                    ft.Container(height=15),
                    ft.Text(
                        "Your Booking Has Been Cancelled",
                        font_family="Sora-Bold",
                        size=22,
                        text_align=ft.TextAlign.CENTER,
                        expand=True,
                        color="#FFFFFF",
                    ),
                    ft.Container(height=10),
                    ft.Text(
                        "We’re sorry to see you go, but we hope to see you again soon! "
                        "If there’s anything we can do to improve your experience, let us know.",
                        font_family="InstrumentSans-Regular",
                        size=14,
                        text_align=ft.TextAlign.CENTER,
                        expand=True,
                        color="#FFFFFF",
                    ),
                    ft.Container(height=30),
                    ft.ElevatedButton(
                        width=self.page.window_width * 0.8,
                        height=50,
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
            padding=ft.Padding(20, 15, 20, 20),
        )

    def on_get_started_click(self, _):
        self.page.go("/homepage")
