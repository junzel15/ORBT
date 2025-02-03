import flet as ft


class CoffeeDetails(ft.UserControl):
    def __init__(self, page: ft.Page, go_to):
        super().__init__()
        self.page = page
        self.go_to = go_to

    def build(self):
        return ft.Container(
            image_src="assets/images/Dark Background 2 Screen.png",
            image_fit=ft.ImageFit.COVER,
            padding=20,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.IconButton(
                                icon=ft.icons.ARROW_BACK,
                                icon_color="white",
                                on_click=lambda _: self.go_to("/"),
                            ),
                            ft.Text("ORBT-BR0001", color="white", weight="bold"),
                        ],
                        alignment="spaceBetween",
                    ),
                    ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Text("COFFEE", color="white", size=10),
                                    ft.Text(
                                        "Dining",
                                        color="white",
                                        font_family="Sora",
                                        size=24,
                                        weight="bold",
                                    ),
                                    ft.Row(
                                        [
                                            ft.Icon(
                                                ft.icons.CALENDAR_MONTH,
                                                color="white",
                                                size=14,
                                            ),
                                            ft.Text(
                                                "Friday, March 15, 2024\n10:30 AM",
                                                color="white",
                                                size=12,
                                            ),
                                        ]
                                    ),
                                    ft.Row(
                                        [
                                            ft.Icon(
                                                ft.icons.LOCATION_ON,
                                                color="white",
                                                size=14,
                                            ),
                                            ft.Text(
                                                "To Be Revealed 🤯",
                                                color="white",
                                                size=12,
                                            ),
                                        ]
                                    ),
                                ]
                            ),
                            ft.Image(
                                src="assets/images/coffee.png", width=100, height=100
                            ),
                        ],
                        alignment="spaceBetween",
                    ),
                    ft.Divider(color="white", thickness=1),
                    ft.Row(
                        [
                            ft.Icon(ft.icons.FAVORITE_BORDER, color="white"),
                            ft.Text(
                                "Common Interests:",
                                color="white",
                                weight="bold",
                                size=14,
                                font_family="Instrument Sans",
                            ),
                        ],
                        spacing=5,
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                ft.Text(
                                    "Technology",
                                    color="white",
                                    size=10,
                                    font_family="Instrument Sans",
                                ),
                                padding=10,
                                border=ft.border.all(1, "white"),
                                border_radius=20,
                            ),
                            ft.Container(
                                ft.Text(
                                    "Politics",
                                    color="white",
                                    size=10,
                                    font_family="Instrument Sans",
                                ),
                                padding=10,
                                border=ft.border.all(1, "white"),
                                border_radius=20,
                            ),
                            ft.Container(
                                ft.Text(
                                    "Healthcare",
                                    color="white",
                                    size=10,
                                    font_family="Instrument Sans",
                                ),
                                padding=10,
                                border=ft.border.all(1, "white"),
                                border_radius=20,
                            ),
                            ft.Container(
                                ft.Text(
                                    "Academia & Research",
                                    color="white",
                                    size=10,
                                    font_family="Instrument Sans",
                                ),
                                padding=10,
                                border=ft.border.all(1, "white"),
                                border_radius=20,
                            ),
                        ],
                        spacing=10,
                        wrap=True,
                        alignment="start",
                    ),
                    ft.Divider(color="white", thickness=1),
                    ft.Row(
                        [
                            ft.Icon(
                                ft.icons.FLAG_CIRCLE,
                                color="white",
                                size=16,
                            ),
                            ft.Text(
                                "Nationality",
                                color="white",
                                weight="bold",
                                width=200,
                                size=14,
                            ),
                            ft.Text(
                                "Language:",
                                color="white",
                                weight="bold",
                                font_family="Instrument Sans",
                                size=14,
                            ),
                        ]
                    ),
                    ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.Image(
                                                src="assets/images/US.png",
                                                width=20,
                                                height=20,
                                            ),
                                            ft.Text(
                                                "United States of America",
                                                color="white",
                                                font_family="Instrument Sans",
                                                size=12,
                                            ),
                                        ]
                                    ),
                                    ft.Row(
                                        [
                                            ft.Image(
                                                src="assets/images/PH.png",
                                                width=20,
                                                height=20,
                                            ),
                                            ft.Text(
                                                "Philippines",
                                                color="white",
                                                font_family="Instrument Sans",
                                                size=12,
                                            ),
                                        ]
                                    ),
                                ]
                            ),
                            ft.Row(
                                [
                                    ft.Text(
                                        "English, Filipino",
                                        color="white",
                                        font_family="Instrument Sans",
                                        size=12,
                                    ),
                                ],
                                alignment="start",
                            ),
                        ],
                        alignment="spaceBetween",
                    ),
                    ft.Divider(color="white", thickness=1),
                    ft.Row(
                        [
                            ft.Icon(
                                ft.icons.STAR,
                                color="white",
                                size=16,
                            ),
                            ft.Text(
                                "Zodiac Signs:",
                                color="white",
                                weight="bold",
                                font_family="Instrument Sans",
                                size=14,
                            ),
                        ]
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.Image(
                                            src="assets/images/Icon Aries.png",
                                            width=25,
                                            height=25,
                                        ),
                                        ft.Text(
                                            "Aries",
                                            color="white",
                                            font_family="Instrument Sans",
                                            size=12,
                                        ),
                                    ]
                                )
                            ),
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.Image(
                                            src="assets/images/Icon Taurus.png",
                                            width=25,
                                            height=25,
                                        ),
                                        ft.Text(
                                            "Taurus",
                                            color="white",
                                            font_family="Instrument Sans",
                                            size=12,
                                        ),
                                    ]
                                )
                            ),
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.Image(
                                            src="assets/images/Icon Gemini.png",
                                            width=25,
                                            height=25,
                                        ),
                                        ft.Text(
                                            "Gemini",
                                            color="white",
                                            font_family="Instrument Sans",
                                            size=12,
                                        ),
                                    ]
                                )
                            ),
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.Image(
                                            src="assets/images/Icon Cancer.png",
                                            width=25,
                                            height=25,
                                        ),
                                        ft.Text(
                                            "Cancer",
                                            color="white",
                                            font_family="Instrument Sans",
                                            size=12,
                                        ),
                                    ]
                                )
                            ),
                        ],
                        spacing=10,
                        alignment="start",
                    ),
                    ft.Divider(color="white", thickness=1),
                    ft.Text(
                        "E-Ticket will be revealed 1 day before the event. Stay tuned!",
                        color="white",
                        size=14,
                        text_align="center",
                        font_family="Instrument Sans",
                    ),
                    ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Container(
                                        ft.Text(
                                            "4",
                                            color="white",
                                            size=16,
                                            weight="bold",
                                            font_family="Instrument Sans",
                                        ),
                                        padding=6,
                                        border=ft.border.all(1, "white"),
                                        border_radius=6,
                                        width=35,
                                        alignment=ft.alignment.center,
                                    ),
                                    ft.Text(
                                        "DAYS",
                                        color="white",
                                        size=10,
                                        text_align="center",
                                        font_family="Instrument Sans",
                                    ),
                                ],
                                alignment="center",
                            ),
                            ft.Container(
                                ft.Text(
                                    ":",
                                    color="white",
                                    size=14,
                                    weight="bold",
                                    font_family="Instrument Sans",
                                ),
                                alignment=ft.alignment.center,
                                padding=6,
                            ),
                            ft.Column(
                                [
                                    ft.Container(
                                        ft.Text(
                                            "10",
                                            color="white",
                                            size=16,
                                            weight="bold",
                                            font_family="Instrument Sans",
                                        ),
                                        padding=6,
                                        border=ft.border.all(1, "white"),
                                        border_radius=6,
                                        width=35,
                                        alignment=ft.alignment.center,
                                    ),
                                    ft.Text(
                                        "HOURS",
                                        color="white",
                                        size=10,
                                        text_align="center",
                                        font_family="Instrument Sans",
                                    ),
                                ],
                                alignment="center",
                            ),
                            ft.Container(
                                ft.Text(
                                    ":",
                                    color="white",
                                    size=14,
                                    weight="bold",
                                    font_family="Instrument Sans",
                                ),
                                alignment=ft.alignment.center,
                                padding=6,
                            ),
                            ft.Column(
                                [
                                    ft.Container(
                                        ft.Text(
                                            "12",
                                            color="white",
                                            size=16,
                                            weight="bold",
                                            font_family="Instrument Sans",
                                        ),
                                        padding=6,
                                        border=ft.border.all(1, "white"),
                                        border_radius=6,
                                        width=35,
                                        alignment=ft.alignment.center,
                                    ),
                                    ft.Text(
                                        "MIN",
                                        color="white",
                                        size=10,
                                        text_align="center",
                                        font_family="Instrument Sans",
                                    ),
                                ],
                                alignment="center",
                            ),
                        ],
                        alignment="center",
                        spacing=5,
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                "Cancel Event",
                                bgcolor="white",
                                color="black",
                                width=150,
                            ),
                            ft.ElevatedButton(
                                "View E-Ticket",
                                bgcolor="#3A1A6A",
                                color="white",
                                width=150,
                            ),
                        ],
                        alignment="center",
                        spacing=10,
                    ),
                ]
            ),
        )
