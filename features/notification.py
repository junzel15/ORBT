import flet as ft
from flet import UserControl


class NotificationPage(ft.UserControl):

    def __init__(self, page, go_to):
        self.go_to = go_to
        super().__init__()
        self.page = page

        self.page.window_width = 400
        self.page.window_height = 735
        self.page.update()

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        ft.Row(
                            controls=[
                                ft.CupertinoButton(
                                    alignment=ft.Alignment(-1, 0),
                                    content=ft.Image(
                                        src="images/back.png",
                                        width=22,
                                        height=22,
                                        fit=ft.ImageFit.FILL,
                                    ),
                                    on_click=lambda e: self.go_to(
                                        "/location", self.page
                                    ),
                                ),
                            ],
                        ),
                        padding=ft.Padding(0, 0, 50, 0),
                    ),
                    ft.Container(
                        content=ft.Text(
                            "Never Miss a Beat",
                            font_family="Sora-SemiBold",
                            size=20,
                            text_align=ft.TextAlign.CENTER,
                            width=240,
                        ),
                    ),
                    ft.Container(
                        content=ft.Text(
                            "Receive updates on exciting events, exclusive offers, and meaningful interactions.",
                            font_family="InstrumentSans-Regular",
                            size=14,
                            text_align=ft.TextAlign.CENTER,
                            width=240,
                        ),
                    ),
                    ft.Container(height=20),
                    ft.Container(
                        content=ft.Image(
                            src="images/notification.png", width=319, height=298
                        ),
                        alignment=ft.alignment.top_center,
                        padding=ft.Padding(0, 0, 0, 0),
                    ),
                    ft.Container(height=60),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.ElevatedButton(
                                    width=1000,
                                    height=50,
                                    text="Allow Notification",
                                    style=ft.ButtonStyle(
                                        text_style=ft.TextStyle(
                                            font_family="InstrumentSans-SemiBold",
                                            size=16,
                                            color=ft.Colors.WHITE,
                                        ),
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                    ),
                                    color=ft.Colors.WHITE,
                                    bgcolor="#5300FA",
                                    on_click=self.on_allow_notification_click,
                                ),
                            ]
                        ),
                        alignment=ft.alignment.top_center,
                        padding=ft.Padding(20, 0, 20, 0),
                    ),
                    ft.Container(height=2),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.TextButton(
                                    "Skip for now",
                                    style=ft.ButtonStyle(
                                        text_style=ft.TextStyle(
                                            font_family="InstrumentSans-Regular",
                                            size=16,
                                            color="#000000",
                                        ),
                                        color="#000000",
                                    ),
                                    on_click=lambda e: self.go_to("/login", self.page),
                                ),
                            ]
                        ),
                        alignment=ft.alignment.top_center,
                        padding=ft.Padding(20, 0, 20, 0),
                    ),
                    ft.Container(height=1000),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            alignment=ft.alignment.top_center,
            bgcolor=ft.Colors.WHITE,
            padding=ft.Padding(20, 0, 20, 10),
        )

    def on_back_click(self, _):
        print("Back Click")
        if self.on_back:
            self.on_back()

    def on_allow_notification_click(self, _):
        if self.on_allow_notification:
            self.on_allow_notification()

    def on_skip_click(self, _):
        if self.on_skip:
            self.on_skip()
