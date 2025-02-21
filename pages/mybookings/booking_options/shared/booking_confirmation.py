import flet as ft
from flet import UserControl


class ConfirmationScreen(ft.UserControl):

    def __init__(self, page, go_to):
        self.go_to = go_to
        super().__init__()
        self.page = page

        self.set_mobile_view()

        self.page.on_resize = self.adjust_window_size
        self.adjust_window_size()
        self.page.update()

    def set_mobile_view(self):
        self.page.window_width = 400
        self.page.window_height = 740

    def adjust_window_size(self, _=None):
        screen_width = self.page.window_width
        screen_height = self.page.window_height

        if screen_width <= 480:
            self.set_mobile_view()
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
                    ft.Container(height=40),
                    ft.Container(
                        content=ft.Image(
                            src="images/Booking Successful.png",
                            width=255,
                            height=321,
                        ),
                        alignment=ft.alignment.top_center,
                        padding=ft.Padding(0, 0, 0, 0),
                    ),
                    ft.Container(
                        content=ft.Text(
                            "Booking Successful!",
                            font_family="Sora-Bold",
                            size=28,
                            text_align=ft.TextAlign.CENTER,
                            width=240,
                            color="#FFFFFF",
                        ),
                    ),
                    ft.Container(
                        content=ft.Text(
                            "Your reservation is confirmed! Tap the button below to view your ticket details.",
                            font_family="InstrumentSans-Regular",
                            size=14,
                            text_align=ft.TextAlign.CENTER,
                            width=240,
                            color="#FFFFFF",
                        ),
                    ),
                    ft.Container(height=20),
                    ft.Container(height=50),
                    ft.Container(
                        padding=ft.Padding(20, 0, 0, 0),
                        content=ft.ElevatedButton(
                            width=1000,
                            height=50,
                            content=ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text(
                                            value="View Booking",
                                            font_family="InstrumentSans-SemiBold",
                                            size=16,
                                            color="#FFFFFF",
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                padding=ft.padding.all(10),
                            ),
                            bgcolor="#5300FA",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=10),
                            ),
                            on_click=self.on_get_started_click,
                        ),
                    ),
                    ft.Container(height=10),
                    ft.Container(height=1000),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            alignment=ft.alignment.top_center,
            image_src="assets/images/Dark Background 2 Screen.png",
            image_fit=ft.ImageFit.COVER,
            padding=ft.Padding(20, 0, 20, 10),
        )

    def on_get_started_click(self, _):
        self.page.go("/bookingdetails")
