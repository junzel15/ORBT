import flet as ft
import json
import os


class AboutMePage(ft.UserControl):
    def __init__(self, page, go_to):
        super().__init__()
        self.go_to = go_to
        self.page = page
        self.about_me_input = None

    def save_about_me(self):
        if not self.about_me_input:
            return

        about_me_text = self.about_me_input.value.strip()
        if not about_me_text:
            return

        if os.path.exists("users.json"):
            with open("users.json", "r") as file:
                try:
                    data = json.load(file)
                    if not isinstance(data, list):
                        data = []
                except json.JSONDecodeError:
                    data = []
        else:
            data = []

        if data:
            data[0]["about_me"] = about_me_text

        with open("users.json", "w") as file:
            json.dump(data, file, indent=4)

        print("About Me saved:", about_me_text)

    def build(self):

        self.about_me_input = ft.TextField(
            height=178,
            hint_text="Something about you ...",
            border=ft.InputBorder.NONE,
            text_style=ft.TextStyle(
                font_family="InstrumentSans-Regular",
                size=16,
                color=ft.Colors.WHITE,
            ),
        )

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        expand=1,
                        height=600,
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    ft.Row(
                                        controls=[
                                            ft.CupertinoButton(
                                                alignment=ft.Alignment(-1, 0),
                                                content=ft.Image(
                                                    src="images/back_white.png",
                                                    width=22,
                                                    height=22,
                                                    fit=ft.ImageFit.FILL,
                                                ),
                                                on_click=lambda e: self.go_to(
                                                    "/birthday", self.page
                                                ),
                                            ),
                                            ft.Container(width=20),
                                            ft.ProgressBar(
                                                width=197,
                                                color="#A87AFE",
                                                bgcolor="#E4DFDF",
                                                value=4 / 5,
                                            ),
                                        ],
                                    ),
                                    padding=ft.Padding(0, 0, 50, 0),
                                ),
                                ft.Container(
                                    width=1000,
                                    height=540,
                                    content=ft.Stack(
                                        controls=[
                                            ft.Image(
                                                src="images/stack_card.png",
                                                width=332,
                                                height=540,
                                            ),
                                            ft.Container(
                                                content=ft.Column(
                                                    height=450,
                                                    controls=[
                                                        ft.Text(
                                                            "About Me",
                                                            font_family="Sora-SemiBold",
                                                            size=20,
                                                            text_align=ft.TextAlign.CENTER,
                                                            color=ft.Colors.WHITE,
                                                            weight=ft.FontWeight.W_700,
                                                            width=300,
                                                        ),
                                                        ft.Container(height=10),
                                                        ft.Container(
                                                            height=218,
                                                            content=ft.Column(
                                                                controls=[
                                                                    self.about_me_input
                                                                ],
                                                            ),
                                                            border_radius=10,
                                                            border=ft.border.all(
                                                                1, "#DFDFE4"
                                                            ),
                                                            padding=ft.Padding(
                                                                20, 20, 20, 20
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                padding=ft.Padding(20, 30, 20, 0),
                                            ),
                                        ],
                                    ),
                                    padding=ft.Padding(20, 0, 20, 0),
                                ),
                            ],
                        ),
                    ),
                    ft.Container(height=7),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.ElevatedButton(
                                    width=1000,
                                    height=50,
                                    text="Next",
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
                                    on_click=lambda e: self.on_next_click(),
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
                                            color=ft.Colors.WHITE,
                                        ),
                                        color="#FFFFFF",
                                    ),
                                    on_click=lambda e: self.go_to(
                                        "/location", self.page
                                    ),
                                ),
                            ]
                        ),
                        alignment=ft.alignment.top_center,
                        padding=ft.Padding(20, 0, 20, 0),
                    ),
                    ft.Container(height=1000),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            padding=ft.Padding(20, 0, 20, 10),
            expand=1,
            alignment=ft.alignment.top_center,
            bgcolor=ft.Colors.BLACK,
        )

    def on_next_click(self):
        self.save_about_me()
        self.go_to("/interest", self.page)
