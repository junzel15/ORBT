import flet as ft
from global_state import get_logged_in_user
from dynamodb.dynamoDB_profiles import dynamo_write


class ProfileEditPage(ft.UserControl):
    def __init__(self, page: ft.Page, go_to: callable = None, user: dict = None):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.user = user or {}
        self.page.title = "Edit Profile"
        self.page.padding = 0
        self.page.scroll = "adaptive"
        self.page.bgcolor = "#F8F9FA"
        self.user = get_logged_in_user() or {}

        self.page.window_width = 400
        self.page.window_height = 680
        self.page.update()

        self.build_ui()
        self.page.add(self.render())

    def input_field(self, icon, label, key, value="", password=False):
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
                        on_change=lambda e: self.update_profile_data(
                            key, e.control.value
                        ),
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

    def update_profile_data(self, key, value):
        user_data = self.page.session.get("user")
        if user_data is None:
            user_data = {}

        if not isinstance(user_data, dict):
            user_data = {}
        user_data[key] = value
        self.page.session.set("user", user_data)
        self.user[key] = value
        self.page.update()

    def dropdown_field(self, icon, label, options, value=""):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Icon(icon, size=20, color="#6c757d"),
                    ft.Dropdown(
                        options=[ft.dropdown.Option(opt) for opt in options],
                        value=value,
                        border=ft.InputBorder.NONE,
                        expand=True,
                        on_change=lambda e: self.update_profile_data(
                            "gender", e.control.value
                        ),
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

    def build_ui(self):
        self.file_picker = ft.FilePicker(on_result=self.upload_image)
        self.page.overlay.append(self.file_picker)

        profile_image = self.user.get("profile_image", "")
        if profile_image:
            avatar_content = ft.Container(
                content=ft.Image(
                    src=profile_image,
                    fit=ft.ImageFit.COVER,
                    width=80,
                    height=80,
                ),
                border_radius=ft.border_radius.all(40),
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
            )
        else:
            avatar_content = ft.Text("C", size=40, weight="bold", color="white")

        self.avatar_image = ft.CircleAvatar(
            radius=40,
            content=avatar_content,
            bgcolor="#CCCCCC",
        )

        self.avatar_section = ft.Container(
            content=ft.Stack(
                controls=[
                    self.avatar_image,
                    ft.Container(
                        content=ft.Icon(ft.icons.EDIT, color="white", size=16),
                        bgcolor="purple",
                        shape=ft.BoxShape.CIRCLE,
                        width=24,
                        height=24,
                        alignment=ft.alignment.center,
                        padding=ft.padding.all(4),
                        on_click=lambda _: self.file_picker.pick_files(
                            allow_multiple=False
                        ),
                    ),
                ],
                alignment=ft.alignment.bottom_right,
            ),
            alignment=ft.alignment.center,
        )

        self.bio_field = ft.Container(
            content=ft.TextField(
                value=self.user.get("bio", ""),
                label="Bio",
                multiline=True,
                border=ft.InputBorder.NONE,
                expand=True,
                on_change=lambda e: self.update_profile_data("bio", e.control.value),
            ),
            padding=ft.padding.symmetric(horizontal=10, vertical=10),
            bgcolor="#FFFFFF",
            border_radius=ft.border_radius.all(8),
            margin=ft.margin.symmetric(vertical=5),
        )

        self.interests_field = ft.TextField(
            hint_text="My Interests",
            border=ft.InputBorder.OUTLINE,
            border_color="#D6D6D6",
            bgcolor="#FFFFFF",
            height=40,
            on_submit=self.add_interest,
        )

        self.interests_list = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Text(interest, size=12, color="white"),
                    bgcolor=color,
                    padding=ft.padding.symmetric(horizontal=10, vertical=5),
                    border_radius=ft.border_radius.all(15),
                    margin=ft.margin.all(5),
                )
                for interest, color in zip(
                    self.user.get("interests", []),
                    [
                        "#6C757D",
                        "#DC3545",
                        "#6F42C1",
                        "#28A745",
                        "#17A2B8",
                        "#DC3545",
                        "#6F42C1",
                        "#28A745",
                    ],
                )
            ],
            wrap=True,
            spacing=5,
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
            self.input_field(
                ft.icons.PERSON,
                "Full Name",
                "full_name",
                self.user.get("full_name", ""),
            ),
            self.input_field(
                ft.icons.EMAIL, "Email", "email", self.user.get("email", "")
            ),
            self.input_field(
                ft.icons.LOCK,
                "Password",
                "password",
                self.user.get("password", ""),
                password=True,
            ),
            self.input_field(
                ft.icons.PHONE,
                "Phone Number",
                "phone_number",
                self.user.get("phone_number", ""),
            ),
            self.dropdown_field(
                ft.icons.WC, "Gender", ["Male", "Female"], self.user.get("gender", "")
            ),
            self.input_field(
                ft.icons.CALENDAR_MONTH,
                "Date of Birth",
                "birthdate",
                self.user.get("birthdate", ""),
            ),
            self.bio_field,
            ft.Text("My Interests", size=16, color="black"),
            self.interests_field,
            self.interests_list,
            self.save_button,
        ]

    def upload_image(self, e: ft.FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path
            self.user["profile_image"] = file_path
            self.page.session.set("user", self.user)

            self.avatar_image.content = ft.Container(
                content=ft.Image(
                    src=file_path,
                    fit=ft.ImageFit.COVER,
                    width=80,
                    height=80,
                ),
                border_radius=ft.border_radius.all(40),
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
            )

            self.avatar_image.update()

            self.update_profile_data("profile_image", file_path)

            self.page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Profile image uploaded!", color="white"),
                    bgcolor="green",
                )
            )

    def add_interest(self, e):
        new_interest = self.interests_field.value.strip()
        if new_interest and new_interest not in self.user.get("interests", []):
            self.user.setdefault("interests", []).append(new_interest)
            self.interests_field.value = ""
            self.update_interests_list()
            self.page.update()

    def update_interests_list(self):
        self.interests_list.controls = [
            ft.Container(
                content=ft.Text(interest, size=12, color="white"),
                bgcolor=color,
                padding=ft.padding.symmetric(horizontal=10, vertical=5),
                border_radius=ft.border_radius.all(15),
                margin=ft.margin.all(5),
            )
            for interest, color in zip(
                self.user.get("interests", []),
                [
                    "#6C757D",
                    "#DC3545",
                    "#6F42C1",
                    "#28A745",
                    "#17A2B8",
                    "#DC3545",
                    "#6F42C1",
                    "#28A745",
                ],
            )
        ]
        self.page.update()

    def save_changes(self, e):
        try:
            updated_user = {
                "full_name": self.main_content[1].content.controls[1].value,
                "email": self.main_content[2].content.controls[1].value,
                "password": self.main_content[3].content.controls[1].value,
                "phone_number": self.main_content[4].content.controls[1].value,
                "gender": self.main_content[5].content.controls[1].value,
                "birthdate": self.main_content[6].content.controls[1].value,
                "bio": self.bio_field.content.value,
                "interests": self.user.get("interests", []),
                "profile_image": self.user.get("profile_image", ""),
            }

            dynamo_write("profiles", updated_user)

            self.page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Changes saved successfully!", color="white"),
                    bgcolor="green",
                )
            )

        except Exception as err:
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
