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
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=[
                        "#5300FA",
                        "#000000",
                        "#000000",
                        "#5300FA",
                    ],
                    stops=[0.0, 0.3, 0.7, 1.0],
                ),
                content=ft.Stack(
                    controls=[
                        ft.Container(
                            alignment=ft.alignment.center,
                            content=ft.Image(
                                src="assets/images/ORBT Logo - Splash Screen.png",
                                fit=ft.ImageFit.CONTAIN,
                                width=200,
                                height=200,
                            ),
                        )
                    ],
                    expand=True,
                ),
            )
        ],
    )
