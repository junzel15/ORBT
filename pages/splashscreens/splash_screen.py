import threading
import flet as ft


class SplashScreen(ft.View):
    def __init__(self, page, go_to):
        super().__init__(
            route="/splash",
            controls=[
                ft.Container(
                    expand=True,
                    content=ft.Stack(
                        controls=[
                            ft.Image(
                                src="images/splash.png",
                                fit=ft.ImageFit.COVER,
                                expand=True,
                            ),
                        ],
                        expand=True,
                    ),
                )
            ],
        )
        self.page = page
        self.go_to = go_to
        self.start_timer()

        self.page.window_width = 330
        self.page.window_height = 680
        self.page.update()

    def start_timer(self):
        def timer_thread():
            import time

            time.sleep(3)
            self.go_to("/onboarding1", self.page)

        threading.Thread(target=timer_thread, daemon=True).start()
