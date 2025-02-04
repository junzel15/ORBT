import flet as ft
import random
import json


class ForgotPassword(ft.UserControl):
    def __init__(self, page, go_to, **kwargs):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.selected_option = "sms"
        self.users = self.load_users()
        self.current_user = self.get_current_user()

    def build(self):

        phone_number = self.current_user.get("phone_number", "Not Available")
        email = self.current_user.get("email", "Not Available")

        self.sms_container = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Icon(ft.icons.MESSAGE, color="#5300FA", size=24),
                        padding=10,
                        bgcolor="#E5D9FF",
                        border_radius=30,
                    ),
                    ft.Column(
                        controls=[
                            ft.Text("via SMS:", size=12, color=ft.colors.GREY),
                            ft.Text(
                                phone_number[:5] + "****",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ]
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            padding=15,
            border=(
                ft.border.all(2, "#5300FA")
                if self.selected_option == "sms"
                else ft.border.all(1, ft.colors.GREY_300)
            ),
            border_radius=15,
            on_click=lambda _: self.select_option("sms"),
            bgcolor="#E5D9FF" if self.selected_option == "sms" else ft.colors.WHITE,
        )

        self.email_container = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Icon(ft.icons.EMAIL, color="#5300FA", size=24),
                        padding=10,
                        bgcolor="#E5D9FF",
                        border_radius=30,
                    ),
                    ft.Column(
                        controls=[
                            ft.Text("via Email:", size=12, color=ft.colors.GREY),
                            ft.Text(
                                email[:5] + "***@gmail.com",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ]
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            padding=15,
            border=(
                ft.border.all(2, "#5300FA")
                if self.selected_option == "email"
                else ft.border.all(1, ft.colors.GREY_300)
            ),
            border_radius=15,
            on_click=lambda _: self.select_option("email"),
            bgcolor="#E5D9FF" if self.selected_option == "email" else ft.colors.WHITE,
        )

        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.ARROW_BACK,
                            icon_size=24,
                            on_click=lambda _: self.go_to("/login"),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Text("Forgot Password", size=24, weight=ft.FontWeight.BOLD),
                ft.Text(
                    "Select which contact detail should we use to reset your password.",
                    size=14,
                    color=ft.colors.GREY,
                ),
                self.sms_container,
                self.email_container,
                ft.Container(height=20),
                ft.ElevatedButton(
                    text="Continue",
                    bgcolor="#5300FA",
                    color=ft.colors.WHITE,
                    height=50,
                    width=300,
                    on_click=self.continue_action,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                ),
            ],
            spacing=15,
        )

    def select_option(self, option):
        self.selected_option = option

        self.sms_container.border = (
            ft.border.all(2, "#5300FA")
            if self.selected_option == "sms"
            else ft.border.all(1, ft.colors.GREY_300)
        )
        self.sms_container.bgcolor = (
            "#E5D9FF" if self.selected_option == "sms" else ft.colors.WHITE
        )

        self.email_container.border = (
            ft.border.all(2, "#5300FA")
            if self.selected_option == "email"
            else ft.border.all(1, ft.colors.GREY_300)
        )
        self.email_container.bgcolor = (
            "#E5D9FF" if self.selected_option == "email" else ft.colors.WHITE
        )

        self.update()

    def continue_action(self, e):
        print(f"Selected option: {self.selected_option}")

        otp = self.generate_otp()
        if self.update_user_otp(self.current_user["email"], otp):

            if self.selected_option == "sms":
                self.send_sms(self.current_user["phone_number"], otp)
            else:
                self.send_email(self.current_user["email"], otp)

            self.go_to("/otp", self.page)
        else:
            self.page.snack_bar = ft.SnackBar(content=ft.Text("User not found"))
            self.page.snack_bar.open = True
            self.page.update()

    def load_users(self):
        try:
            with open("json/users.json", "r") as file:
                return json.load(file)
        except Exception as e:
            print(f"Error loading users.json: {e}")
            return []

    def get_current_user(self):

        return self.users[0] if self.users else {}

    def generate_otp(self):
        return str(random.randint(1000, 9999))

    def update_user_otp(self, email, otp):
        for user in self.users:
            if user["email"] == email:
                user["otp"]["reset_password"] = otp
                with open("json/users.json", "w") as file:
                    json.dump(self.users, file, indent=4)
                return True
        return False

    def send_sms(self, phone_number, otp):

        print(f"Sending SMS to {phone_number}: OTP {otp}")

    def send_email(self, email, otp):

        print(f"Sending Email to {email}: OTP {otp}")
