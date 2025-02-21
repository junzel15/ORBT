import flet as ft
import json
import bcrypt


class ResetPasswordPage(ft.UserControl):
    def __init__(self, page: ft.Page, go_to):
        super().__init__()
        self.page = page
        self.go_to = go_to

        self.page.window_width = 380
        self.page.window_height = 680
        self.page.update()

        self.password = ft.TextField(
            label="New Password",
            password=True,
            can_reveal_password=True,
            on_change=self.validate_password,
        )
        self.confirm_password = ft.TextField(
            label="Confirm Password",
            password=True,
            can_reveal_password=True,
            on_change=self.validate_password,
        )
        self.requirements = [
            ("At least 8 characters", False),
            ("At least 1 number", False),
            ("Both upper and lowercase letters", False),
        ]
        self.requirement_texts = [
            ft.Row(
                [
                    ft.Icon(ft.icons.CHECK_CIRCLE, color="#27CD7E", visible=False),
                    ft.Text(
                        req, font_family="Instrument Sans", size=12, color="#27CD7E"
                    ),
                ]
            )
            for req, _ in self.requirements
        ]
        self.reset_button = ft.ElevatedButton(
            "Reset Password",
            disabled=True,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
            on_click=self.reset_password,
        )

    def validate_password(self, e):
        password = self.password.value
        passwords_match = password == self.confirm_password.value
        self.reset_button.disabled = not passwords_match
        self.update()

    def reset_password(self, e):

        new_password = self.password.value

        hashed_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())

        with open("json/users.json", "r") as file:
            users = json.load(file)

        for user in users:
            if user["email"] == "elvis@gmail.com":
                user["password"] = hashed_password.decode()
                break

        with open("json/users.json", "w") as file:
            json.dump(users, file)

        print("Password has been reset successfully!")
        self.go_to("/confirmationpassword", self.page)

    def hash_password(self, password):

        import hashlib

        return hashlib.sha256(password.encode()).hexdigest()

    def build(self):
        return ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.ARROW_BACK,
                            on_click=lambda _: self.go_to("/otp"),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Text("Create new password", size=22, weight=ft.FontWeight.BOLD),
                ft.Text(
                    "Your new password must be different from the previous password."
                ),
                self.password,
                self.confirm_password,
                *self.requirement_texts,
                self.reset_button,
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
