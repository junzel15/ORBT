import flet as ft
from flet import UserControl


class CancelBooking(UserControl):
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
        self.page.window_height = 780

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
                    ft.Container(height=10),
                    ft.Container(
                        alignment=ft.alignment.top_left,
                        content=ft.IconButton(
                            icon=ft.icons.ARROW_BACK_IOS_NEW,
                            icon_color="white",
                            on_click=lambda _: self.page.go("/bookingdetails"),
                        ),
                    ),
                    ft.Text(
                        "Cancel Booking",
                        size=26,
                        weight=ft.FontWeight.BOLD,
                        color="white",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(height=5),
                    ft.Text(
                        "Please select the reason for cancellation:",
                        size=14,
                        color="white",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(height=15),
                    ft.Container(
                        padding=ft.Padding(15, 15, 15, 15),
                        border_radius=12,
                        bgcolor="white",
                        content=ft.Column(
                            controls=[
                                ft.RadioGroup(
                                    content=ft.Column(
                                        [
                                            ft.Radio(
                                                value="change", label="Change in Plans"
                                            ),
                                            ft.Radio(
                                                value="health", label="Health Issues"
                                            ),
                                            ft.Radio(
                                                value="work", label="Unexpected Work"
                                            ),
                                            ft.Radio(
                                                value="preferences",
                                                label="Personal Preferences",
                                            ),
                                            ft.Radio(
                                                value="conflicts",
                                                label="Scheduling Conflicts",
                                            ),
                                            ft.Radio(value="other", label="Other"),
                                        ]
                                    ),
                                ),
                                ft.Container(height=8),
                                ft.TextField(
                                    hint_text="Please specify",
                                    multiline=True,
                                    border_radius=5,
                                    border_color="#cccccc",
                                    height=100,
                                ),
                            ],
                        ),
                    ),
                    ft.Container(height=20),
                    ft.ElevatedButton(
                        width="100%",
                        height=55,
                        content=ft.Text(
                            "Cancel Booking",
                            size=16,
                            color="white",
                            font_family="InstrumentSans-SemiBold",
                        ),
                        bgcolor="#5300FA",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                        ),
                        on_click=self.on_cancel_booking,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            alignment=ft.alignment.top_center,
            image_src="assets/images/Dark Background 2 Screen.png",
            image_fit=ft.ImageFit.COVER,
            padding=ft.Padding(20, 20, 20, 20),
        )

    def on_cancel_booking(self, _):
        self.page.go("/cancelsuccessfull")
