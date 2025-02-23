import threading
import flet as ft
from flet import UserControl


class LoadingScreen(ft.UserControl):
    def __init__(self, page, go_to):
        self.page = page
        self.go_to = go_to

        self.page.window_width = 400
        self.page.window_height = 750
        self.page.update()

        super().__init__()
        self.start_timer()

    def build(self):
        screen_width = self.page.window_width

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(height=40),
                    ft.Container(
                        content=ft.Image(
                            src="images/Loading Screen.png",
                            width=min(255, screen_width * 0.6),
                            height=min(321, screen_width * 0.75),
                        ),
                        alignment=ft.alignment.top_center,
                    ),
                    ft.Container(
                        content=ft.Text(
                            "Matching You with Your Crew...",
                            font_family="Sora-Bold",
                            size=(28 if screen_width > 600 else 22),
                            text_align=ft.TextAlign.CENTER,
                            width=min(240, screen_width * 0.8),
                            color="#FFFFFF",
                        ),
                    ),
                    ft.Container(
                        content=ft.Text(
                            "Our algorithm is curating the perfect group for your upcoming adventure. "
                            "Hang tight—your plans are coming together!",
                            font_family="InstrumentSans-Regular",
                            size=14 if screen_width > 600 else 12,
                            text_align=ft.TextAlign.CENTER,
                            width=min(240, screen_width * 0.8),
                            color="#FFFFFF",
                        ),
                    ),
                    ft.Container(height=20),
                    ft.Container(height=120 if screen_width > 600 else 80),
                    ft.Container(height=10),
                    ft.Container(height=screen_width * 1.5),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            alignment=ft.alignment.top_center,
            bgcolor=ft.colors.WHITE,
            padding=ft.Padding(
                20 if screen_width > 600 else 10,
                0,
                20 if screen_width > 600 else 10,
                10,
            ),
            image_src="assets/images/Dark Background 2 Screen.png",
            image_fit=ft.ImageFit.COVER,
        )

    def start_timer(self):
        def timer_thread():
            import time

            time.sleep(2)
            self.go_to("/bookingconfirmation", self.page)

        threading.Thread(target=timer_thread, daemon=True).start()
