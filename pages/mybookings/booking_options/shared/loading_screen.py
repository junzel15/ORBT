import threading
import flet as ft


class LoadingScreen(ft.UserControl):
    def __init__(self, page, go_to):

        self.page = page
        self.go_to = go_to

        super().__init__()
        self.start_timer()

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(height=40),
                    ft.Container(
                        content=ft.Image(
                            src="assets/images/Loading Screen.png",
                            width=255,
                            height=321,
                        ),
                        alignment=ft.alignment.top_center,
                        padding=ft.Padding(0, 0, 0, 0),
                    ),
                    ft.Container(
                        content=ft.Text(
                            "Matching You with Your Crew...",
                            font_family="Sora-Bold",
                            size=28,
                            text_align=ft.TextAlign.CENTER,
                            width=240,
                            color="#FFFFFF",
                        ),
                    ),
                    ft.Container(
                        content=ft.Text(
                            "Our algorithm is curating the perfect group for your upcoming adventure. "
                            "Hang tight—your plans are coming together!",
                            font_family="InstrumentSans-Regular",
                            size=14,
                            text_align=ft.TextAlign.CENTER,
                            width=240,
                            color="#FFFFFF",
                        ),
                    ),
                    ft.Container(height=20),
                    ft.Container(height=120),
                    ft.Container(height=10),
                    ft.Container(height=1000),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            alignment=ft.alignment.top_center,
            bgcolor=ft.colors.WHITE,
            padding=ft.Padding(20, 0, 20, 10),
            image_src="assets/images/Dark Background 2 Screen.png",
            image_fit=ft.ImageFit.COVER,
        )

    def start_timer(self):
        def timer_thread():
            import time

            time.sleep(2)
            self.go_to("/bookingconfirmation", self.page)

        threading.Thread(target=timer_thread, daemon=True).start()
