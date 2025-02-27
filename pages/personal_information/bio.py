import flet as ft
from flet import UserControl
from dynamodb.dynamoDB_profiles import dynamo_write


class BioPage(ft.UserControl):

    def __init__(self, page, go_to, user_email=None):
        super().__init__()
        self.go_to = go_to
        self.page = page
        self.bio_input = None

        self.user_email = user_email

        self.page.window_width = 420
        self.page.window_height = 790
        self.page.update()

    def save_bio_and_next(self):
        if not self.bio_input or not self.bio_input.value.strip():
            print("Bio input is empty or not available.")
            return

        bio_text = self.bio_input.value.strip()

        try:
            user_email = self.user_email
            if not user_email:
                print("User email not found")
                return
            dynamo_write("profiles", {"email": user_email, "bio": bio_text})
            print(f"Bio '{bio_text}' saved for user {user_email}")

        except Exception as e:
            print(f"Error saving bio: {e}")

        self.go_to("/interest", self.page, user_email=user_email)

    def build(self):
        self.bio_input = ft.TextField(
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
                                                    "/birthdate", self.page
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
                                                            "Bio",
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
                                                                    self.bio_input
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
        self.save_bio_and_next()
