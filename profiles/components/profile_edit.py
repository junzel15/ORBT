import flet as ft
import json
from utils.data_provider import get_user_data


class ProfileEditPage(ft.UserControl):
    def __init__(self, page: ft.Page, go_to: callable = None):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.page.title = "Edit Profile"
        self.page.padding = 0
        self.page.scroll = "adaptive"
        self.page.bgcolor = "#F8F9FA"
        self.user_name = None
        self.bio = None
        self.main_content = None
        self.build_ui()

    def build_ui(self):

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
                alignment=ft.alignment.bottom_right,
            ),
            alignment=ft.alignment.center,
        )

        self.bio_field = ft.Container(
            content=ft.TextField(
                value=self.bio or "",
                label="Bio",
                multiline=True,
                border=ft.InputBorder.NONE,
                expand=True,
            ),
            padding=ft.padding.symmetric(horizontal=10, vertical=10),
            bgcolor="#FFFFFF",
            border_radius=ft.border_radius.all(8),
            margin=ft.margin.symmetric(vertical=5),
        )

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
                                content=ft.Text(interest, size=12, color="white"),
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

        self.save_button = ft.Container(
            content=ft.ElevatedButton(
                text="Save changes",
                style=ft.ButtonStyle(
                    color="#FFFFFF",
                    bgcolor="#A2A8BF",
                    padding=ft.padding.symmetric(horizontal=40, vertical=20),
                ),
                on_click=self.save_changes,
            ),
            width=300,
            height=60,
            alignment=ft.alignment.center,
            margin=ft.margin.symmetric(vertical=10),
        )

        self.main_content = [
            self.avatar_section,
            input_field(ft.icons.PERSON, "Full Name", self.user_name or "New Name"),
            input_field(ft.icons.EMAIL, "Email", "newemail@example.com"),
            input_field(ft.icons.LOCK, "Password", "newpassword", password=True),
            input_field(ft.icons.PHONE, "Phone Number", "+63 9123456789"),
            dropdown_field(ft.icons.WC, "Gender", ["Male", "Female"], "Male"),
            input_field(ft.icons.CALENDAR_MONTH, "Date of Birth", "09/12/1990"),
            self.bio_field,
            self.interests_section,
            self.save_button,
        ]

    def save_changes(self, e):
        try:
            self.user_name = self.main_content[1].content.controls[1].value
            self.bio = self.bio_field.content.value

            users_data = get_user_data()

            for user in users_data:
                if user["email"] == "junz@gmail.com":
                    user["full_name"] = self.user_name
                    user["bio"] = self.bio
                    break

            with open("users.json", "w") as f:
                json.dump(users_data, f, indent=4)

            self.page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Changes saved successfully!", color="white"),
                    bgcolor="green",
                )
            )
        except Exception as err:
            print(f"Error saving changes: {err}")
            self.page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text(
                        "Failed to save changes. Please try again.", color="white"
                    ),
                    bgcolor="red",
                )
            )

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
                            controls=self.main_content, spacing=10, padding=10
                        ),
                        expand=True,
                    ),
                ],
                spacing=0,
            ),
            bgcolor="#F8F9FA",
            expand=True,
        )
