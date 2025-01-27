import flet as ft


class GenderPage(ft.UserControl):

    def __init__(self, page, go_to):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.selected_button = None
        self.previous_selected_button = None
        self.buttons = {}

    def build(self):
        print("build(self)")
        self.buttons = {
            "male": self.create_button(
                "images/icon_male_normal.png",
                "images/icon_male_selected.png",
                "Male",
                "male",
            ),
            "female": self.create_button(
                "images/icon_female_normal.png",
                "images/icon_female_selected.png",
                "Female",
                "female",
            ),
            "non_binary": self.create_button(
                "images/icon_non_binary_normal.png",
                "images/icon_non_binary_selected.png",
                "Non-binary",
                "non_binary",
            ),
            "prefer_not": self.create_button(
                "images/icon_x_normal.png",
                "images/icon_x_selected.png",
                "Prefer not to say",
                "prefer_not",
            ),
        }

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
                                                    "/usersetup", self.page
                                                ),
                                            ),
                                            ft.Container(width=20),
                                            ft.ProgressBar(
                                                width=197,
                                                color="#A87AFE",
                                                bgcolor="#E4DFDF",
                                                value=1 / 5,
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
                                                    controls=[
                                                        ft.Text(
                                                            "How do you identify?",
                                                            font_family="Sora-SemiBold",
                                                            size=20,
                                                            text_align=ft.TextAlign.START,
                                                            color=ft.Colors.WHITE,
                                                            weight=ft.FontWeight.W_700,
                                                        ),
                                                        *[
                                                            ft.Row(
                                                                controls=[
                                                                    self.buttons[
                                                                        button_id
                                                                    ]
                                                                ],
                                                                alignment=ft.MainAxisAlignment.START,
                                                            )
                                                            for button_id in self.buttons
                                                        ],
                                                    ],
                                                    alignment=ft.MainAxisAlignment.START,
                                                ),
                                                padding=ft.Padding(30, 30, 30, 0),
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
                                    on_click=lambda e: self.go_to(
                                        "/birthday", self.page
                                    ),
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
                                        color=ft.Colors.WHITE,
                                    ),
                                    on_click=lambda e: self.go_to(
                                        "/aboutme", self.page
                                    ),
                                ),
                            ]
                        ),
                        alignment=ft.alignment.top_center,
                        padding=ft.Padding(20, 0, 20, 0),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            padding=ft.Padding(20, 0, 20, 10),
            expand=1,
            alignment=ft.alignment.top_center,
            bgcolor=ft.Colors.BLACK,
        )

    def create_button(self, default_icon, selected_icon, label, button_id):
        is_selected = self.selected_button == button_id
        return ft.ElevatedButton(
            content=ft.Container(
                content=ft.Row(
                    [
                        ft.Image(
                            src=selected_icon if is_selected else default_icon,
                            width=20,
                            height=20,
                        ),
                        ft.Container(width=15),
                        ft.Text(
                            value=label,
                            font_family="InstrumentSans-Regular",
                            size=16,
                            text_align=ft.TextAlign.START,
                            color="#5300FA" if is_selected else ft.Colors.WHITE,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=5,
                ),
                width=260,
                padding=ft.Padding(20, 20, 20, 20),
            ),
            style=self.get_button_style(is_selected),
            on_click=lambda _: self.on_button_click(button_id),
        )

    def get_button_style(self, is_selected):
        return ft.ButtonStyle(
            bgcolor="#FFFFFF" if is_selected else ft.Colors.TRANSPARENT,
            text_style=ft.TextStyle(
                color="#5300FA" if is_selected else ft.Colors.WHITE,
            ),
            shape=ft.RoundedRectangleBorder(radius=10),
            side={
                ft.ControlState.DEFAULT: ft.BorderSide(1, "#FFFFFF"),
            },
        )

    def on_button_click(self, button_id):
        if button_id == self.selected_button:
            return
        self.previous_selected_button = self.selected_button
        self.selected_button = button_id
        if self.previous_selected_button:
            self.update_button(self.previous_selected_button, False)
        self.update_button(self.selected_button, True)

    def update_button(self, button_id, is_selected):
        button = self.buttons[button_id]
        button.content.content.controls[0].src = (
            f"images/icon_{button_id}_selected.png"
            if is_selected
            else f"images/icon_{button_id}_normal.png"
        )
        button.content.content.controls[2].color = (
            "#5300FA" if is_selected else ft.Colors.WHITE
        )
        button.content.content.controls[2].font_family = (
            "InstrumentSans-Bold" if is_selected else "InstrumentSans-Regular"
        )
        button.style = self.get_button_style(is_selected)
        button.update()
