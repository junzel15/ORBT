import flet as ft
from flet import UserControl
import urllib.parse


class ConfirmationScreen(ft.UserControl):
    def __init__(self, page, go_to):
        super().__init__()
        self.go_to = go_to
        self.page = page
        self.booking_id = self.get_query_param("booking_id")

        self.page.window_width = 400
        self.page.window_height = 750
        self.page.update()

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
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(height=40),
                    ft.Container(
                        content=ft.Image(
                            src="images/Booking Successful.png",
                            width=255,
                            height=321,
                        ),
                        alignment=ft.alignment.top_center,
                    ),
                    ft.Text(
                        "Booking Successful!",
                        font_family="Sora-Bold",
                        size=28,
                        text_align=ft.TextAlign.CENTER,
                        color="#FFFFFF",
                    ),
                    ft.Text(
                        "Your reservation is confirmed! Tap below to view your booking details.",
                        font_family="InstrumentSans-Regular",
                        size=14,
                        text_align=ft.TextAlign.CENTER,
                        color="#FFFFFF",
                    ),
                    ft.Container(height=20),
                    ft.ElevatedButton(
                        width="100%",
                        height=55,
                        content=ft.Text(
                            "View Booking",
                            size=16,
                            color="white",
                            font_family="InstrumentSans-SemiBold",
                        ),
                        bgcolor="#5300FA",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                        ),
                        on_click=lambda _: self.page.go(
                            f"/bookingdetails?booking_id={self.booking_id}"
                            if self.booking_id
                            else "/bookingdetails"
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            bgcolor=ft.colors.WHITE,
            image_src="assets/images/Dark Background 2 Screen.png",
            image_fit=ft.ImageFit.COVER,
        )
