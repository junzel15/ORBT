import threading
import flet as ft


def SplashScreen(page, go_to):

    def start_timer():

        def timer_thread():
            import time

            time.sleep(2)
            page.go("/onboarding1")

        threading.Thread(target=timer_thread, daemon=True).start()

    start_timer()

    return ft.View(
        "/",
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
