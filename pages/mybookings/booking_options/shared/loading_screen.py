import flet as ft
from flet import UserControl
import threading
import time
import urllib.parse


class LoadingScreen(ft.UserControl):
    def __init__(self, page, go_to):
        super().__init__()
        self.page = page
        self.go_to = go_to

        self.booking_id = self.get_query_param("booking_id")

        if not self.booking_id:
            print("Booking ID is missing in LoadingScreen! Aborting navigation.")

        self.page.window_width = 400
        self.page.window_height = 750
        self.page.update()

        self.start_timer()

    def get_query_param(self, param_name):
        try:
            if not self.page or not self.page.route:
                print(" No valid route found, cannot extract query parameters.")
                return None

            if "?" not in self.page.route:
                print(f" Route does not contain query parameters: {self.page.route}")
                return None

            query_string = self.page.route.split("?", 1)[1]
            params = dict(urllib.parse.parse_qsl(query_string))
            print(f"Extracted params: {params}")
            return params.get(param_name)

        except Exception as e:
            print(f"Error parsing query param: {e}")
            return None

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
                    ft.Text(
                        "Matching You with Your Crew...",
                        font_family="Sora-Bold",
                        size=(28 if screen_width > 600 else 22),
                        text_align=ft.TextAlign.CENTER,
                        color="#FFFFFF",
                    ),
                    ft.Container(height=10),
                    ft.Text(
                        "Hang tight—your plans are coming together!",
                        font_family="InstrumentSans-Regular",
                        size=14,
                        text_align=ft.TextAlign.CENTER,
                        color="#FFFFFF",
                    ),
                    ft.Container(height=20),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            bgcolor=ft.colors.WHITE,
            image_src="assets/images/Dark Background 2 Screen.png",
            image_fit=ft.ImageFit.COVER,
        )

    def start_timer(self):
        if not self.booking_id:
            print("Booking ID is missing. Aborting navigation.")
            return

        print(f"⏳ Starting 2-second delay before navigating to bookingconfirmation...")
        threading.Thread(
            target=self.timer_thread, args=(self.booking_id,), daemon=True
        ).start()

    def timer_thread(self, booking_id):
        if not booking_id:
            print("Booking ID is missing. Navigation failed.")
            return

        time.sleep(2)
        print(f"Navigating to bookingconfirmation with ID: {booking_id}")
        self.page.go(f"/bookingconfirmation?booking_id={booking_id}")
