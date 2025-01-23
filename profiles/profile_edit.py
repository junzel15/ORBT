import flet as ft


class ProfileEditPage(ft.UserControl):
    def __init__(self, page: ft.Page, go_to: callable = None):
        super().__init__()
        self.page = page
        self.go_to = go_to

        self.page.title = "Edit Profile"
        self.page.padding = 0
        self.page.scroll = "adaptive"
        self.page.bgcolor = "#F8F9FA"

        self.main_content = None
        self.build_ui()

    def build_ui(self):
        # Avatar section
        self.avatar_section = ft.Container(
            content=ft.Stack(
                controls=[
                    ft.CircleAvatar(
                        content=ft.Text("C", size=40, weight="bold", color="white"),
                        radius=40,
                        bgcolor="#CCCCCC",
                    ),
                    ft.Container(
                        content=ft.Icon(ft.icons.EDIT, color="white", size=16),
                        bgcolor="purple",
                        shape=ft.BoxShape.CIRCLE,
                        width=24,
                        height=24,
                        alignment=ft.alignment.center,
                        padding=ft.padding.all(4),
                    ),
                ],
                width=80,
                height=80,
                alignment=ft.alignment.bottom_right,
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
            ),
            alignment=ft.alignment.center,
        )

        # Input field component
        def input_field(icon, label, value="", password=False):
            return ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(icon, size=20, color="#6c757d"),
                        ft.TextField(
                            value=value,
                            label=label,
                            password=password,
                            border=ft.InputBorder.NONE,
                            expand=True,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10,
                ),
                padding=ft.padding.symmetric(horizontal=10, vertical=10),
                bgcolor="#FFFFFF",
                border_radius=ft.border_radius.all(8),
                margin=ft.margin.symmetric(vertical=5),
            )

        # Dropdown field component
        def dropdown_field(icon, label, options, value=""):
            return ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(icon, size=20, color="#6c757d"),
                        ft.Dropdown(
                            options=[ft.dropdown.Option(opt) for opt in options],
                            value=value,
                            border=ft.InputBorder.NONE,
                            expand=True,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10,
                ),
                padding=ft.padding.symmetric(horizontal=10, vertical=10),
                bgcolor="#FFFFFF",
                border_radius=ft.border_radius.all(8),
                margin=ft.margin.symmetric(vertical=5),
            )

        # Bio field component
        self.bio_field = ft.Container(
            content=ft.Column(
                [
                    ft.Text("My Bio", size=14, weight="bold", color="#000000"),
                    ft.TextField(
                        multiline=True,
                        value="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna.",
                        border=ft.InputBorder.NONE,
                        expand=True,
                    ),
                ],
                spacing=10,
            ),
            padding=ft.padding.all(10),
            bgcolor="#FFFFFF",
            border_radius=ft.border_radius.all(8),
            margin=ft.margin.symmetric(vertical=5),
        )

        # Interests section
        self.interests_section = ft.Container(
            content=ft.Column(
                [
                    ft.Text("My Interests", size=14, weight="bold", color="#000000"),
                    ft.TextField(
                        hint_text="Add Interests",
                        border=ft.InputBorder.OUTLINE,
                        border_color="#D6D6D6",
                        bgcolor="#FFFFFF",
                        height=40,
                    ),
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Text(
                                    interest,
                                    size=12,
                                    weight="bold",
                                    color="white",
                                ),
                                bgcolor=color,
                                padding=ft.padding.symmetric(horizontal=10, vertical=5),
                                border_radius=ft.border_radius.all(15),
                                margin=ft.margin.all(5),
                            )
                            for interest, color in [
                                ("Online Games", "#6C757D"),
                                ("Concert", "#DC3545"),
                                ("R&B Music", "#DC3545"),
                                ("Art", "#6F42C1"),
                                ("Movies", "#28A745"),
                                ("Coffee", "#17A2B8"),
                            ]
                        ],
                        wrap=True,
                        spacing=5,
                    ),
                ],
                spacing=10,
            ),
            padding=ft.padding.all(10),
            bgcolor="#FFFFFF",
            border_radius=ft.border_radius.all(8),
            margin=ft.margin.symmetric(vertical=5),
        )

        # Save button
        self.save_button = ft.Container(
            content=ft.ElevatedButton(
                text="Save changes",
                style=ft.ButtonStyle(
                    color="#FFFFFF",
                    bgcolor="#A2A8BF",
                    padding=ft.padding.symmetric(horizontal=40, vertical=20),
                ),
            ),
            width=300,
            height=60,
            alignment=ft.alignment.center,
            margin=ft.margin.symmetric(vertical=10),
        )

        # Main content collection
        self.main_content = [
            self.avatar_section,
            input_field(ft.icons.PERSON, "Full Name", "New Name"),
            input_field(ft.icons.EMAIL, "Email", "newemail@example.com"),
            input_field(ft.icons.LOCK, "Password", "newpassword", password=True),
            input_field(ft.icons.PHONE, "Phone Number", "+63 9123456789"),
            dropdown_field(ft.icons.WC, "Gender", ["Male", "Female"], "Male"),
            input_field(ft.icons.CALENDAR_MONTH, "Date of Birth", "09/12/1990"),
            self.bio_field,
            self.interests_section,
            self.save_button,
        ]

    def render(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.icons.ARROW_BACK,
                                    icon_size=24,
                                    on_click=lambda e: self.go_to(
                                        "/profile/settings", self.page
                                    ),
                                ),
                                ft.Text("Edit Profile", size=20, weight="bold"),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            spacing=10,
                        ),
                        padding=ft.padding.symmetric(horizontal=10, vertical=15),
                    ),
                    ft.Container(
                        content=ft.ListView(
                            controls=self.main_content,
                            spacing=10,
                            padding=10,
                        ),
                        expand=True,
                        height=600,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=0,
            ),
            bgcolor="#F8F9FA",
            padding=ft.padding.symmetric(horizontal=10),
            expand=True,
        )
