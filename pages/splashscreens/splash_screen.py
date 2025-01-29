import threading
import flet as ft


class SplashScreen(ft.View):
    def __init__(self, page, go_to):
        super().__init__(
            route="/",
            controls=[
                ft.Container(
                    expand=True,
                    content=ft.Stack(
                        controls=[
                            ft.Image(
                                src="assets/images/splash.png",
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

    def start_timer(self):
        def timer_thread():
            import time

            time.sleep(20)
            self.page.go("/onboarding1")

        threading.Thread(target=timer_thread, daemon=True).start()
