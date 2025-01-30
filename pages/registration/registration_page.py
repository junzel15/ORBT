import flet as ft
import json
import bcrypt
import re
import random
from pages.registration.components.customtextfield import CustomTextField
from pages.registration.components.country_code_selector import CountryPhoneCodeSelector
from pages.registration.components.country_data import load_country_data


class RegistrationPage(ft.UserControl):
    def __init__(self, page, go_to):
        self.go_to = go_to
        super().__init__()
        self.page = page
        self.countries = load_country_data()

        self.error_message = ft.Text(visible=False)
        self.full_name_input = CustomTextField(
            hint_text="Full name", left_icon=ft.Icons.PERSON
        )
        self.email_input = CustomTextField(hint_text="Email", left_icon=ft.Icons.EMAIL)
        self.password_input = CustomTextField(
            hint_text="Password",
            left_icon=ft.Icons.LOCK,
            right_icon=ft.Icons.VISIBILITY_OFF,
            is_password=True,
        )
        self.country_phone_code_selector = CountryPhoneCodeSelector(self.countries)

    def is_valid_email(self, email):
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None

    def is_email_unique(self, email):
        try:
            with open("users.json", "r") as file:
                users = json.load(file)
                return not any(user["email"] == email for user in users)
        except FileNotFoundError:
            return True

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def save_user_to_json(self, user_data):
        try:
            with open("users.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.append(user_data)

        with open("users.json", "w") as file:
            json.dump(data, file, indent=4)

    def generate_otp(self):
        return str(random.randint(1000, 9999))

    def register_user(self, e):
        full_name = self.full_name_input.value.strip()
        email = self.email_input.value.strip()
        password = self.password_input.value
        phone_number = self.country_phone_code_selector.phone_code.value

        if not full_name or not email or not password or not phone_number:
            self.error_message.value = "All fields must be filled!"
            self.error_message.visible = True
            self.page.update()
            return

        if not self.is_valid_email(email):
            self.error_message.value = "Invalid email format!"
            self.error_message.visible = True
            self.page.update()
            return

        if not self.is_email_unique(email):
            self.error_message.value = "Email already registered!"
            self.error_message.visible = True
            self.page.update()
            return

        otp = self.generate_otp()
        print(f"Generated OTP: {otp}")

        password_hashed = self.hash_password(password)

        user_data = {
            "id": random.randint(1000, 9999),
            "full_name": full_name,
            "email": email,
            "password": password_hashed,
            "phone_number": phone_number,
            "address": "",
            "gender": "",
            "birthdate": "",
            "bio": "",
            "interests": [],
            "otp": otp,
            "verified": False,
        }

        self.save_user_to_json(user_data)

        self.error_message.value = "Account created successfully! OTP sent."
        self.error_message.color = "green"
        self.error_message.visible = True
        self.page.update()

        self.page.go("/verification")

    def build(self):
        return ft.Container(
            expand=1,
            content=ft.Stack(
                expand=True,
                controls=[
                    ft.Container(
                        content=ft.Image(
                            src="images/registration_bg.png",
                            width=1000,
                            fit=ft.ImageFit.COVER,
                            expand=True,
                        ),
                        expand=True,
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Container(height=30),
                                ft.Container(
                                    content=ft.Image(
                                        src="images/logo_blue.png", width=145, height=42
                                    ),
                                    alignment=ft.alignment.top_center,
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(
                                            "Create an Account",
                                            font_family="Sora-SemiBold",
                                            size=24,
                                            text_align=ft.TextAlign.CENTER,
                                        )
                                    ],
                                ),
                                ft.Text(
                                    "Fill your information below or register with your social account."
                                ),
                                ft.Container(height=5),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            self.full_name_input,
                                            self.email_input,
                                            self.password_input,
                                            self.country_phone_code_selector,
                                        ],
                                        spacing=15,
                                    ),
                                ),
                                self.error_message,
                                ft.Checkbox(
                                    label="Agree with Terms & Condition",
                                    width=300,
                                    label_style=ft.TextStyle(
                                        font_family="Instrument Sans",
                                        size=12,
                                    ),
                                ),
                                ft.Container(
                                    content=ft.ElevatedButton(
                                        "Register",
                                        width=1000,
                                        height=50,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=10)
                                        ),
                                        bgcolor=ft.Colors.BLUE,
                                        color=ft.Colors.WHITE,
                                        on_click=self.register_user,
                                    ),
                                    padding=ft.Padding(0, 0, 0, 0),
                                ),
                                ft.Container(height=10),
                                ft.Row(
                                    controls=[
                                        ft.Divider(),
                                        ft.Text("Or continue with"),
                                        ft.Divider(),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                ft.Container(height=10),
                                ft.Container(
                                    height=50,
                                    bgcolor=ft.Colors.TRANSPARENT,
                                    content=ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                        controls=[
                                            ft.ElevatedButton(
                                                expand=True,
                                                content=ft.Row(
                                                    [
                                                        ft.Image(
                                                            src="images/icon_google.png",
                                                            width=24,
                                                            height=24,
                                                            fit=ft.ImageFit.COVER,
                                                        ),
                                                    ],
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                ),
                                                height=50,
                                                style=ft.ButtonStyle(
                                                    shape=ft.RoundedRectangleBorder(
                                                        radius=10
                                                    ),
                                                ),
                                            ),
                                            ft.Container(width=20),
                                            ft.ElevatedButton(
                                                expand=True,
                                                content=ft.Row(
                                                    [
                                                        ft.Image(
                                                            src="images/icon_fb.png",
                                                            width=18,
                                                            height=18,
                                                            fit=ft.ImageFit.COVER,
                                                        ),
                                                    ],
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                ),
                                                height=50,
                                                style=ft.ButtonStyle(
                                                    shape=ft.RoundedRectangleBorder(
                                                        radius=10
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                ft.Container(height=10),
                                ft.Row(
                                    controls=[
                                        ft.Text("Already have account? "),
                                        ft.TextButton(
                                            "Log in", on_click=self.on_login_click
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=0,
                                ),
                            ],
                            spacing=10,
                        ),
                        padding=ft.Padding(20, 0, 20, 0),
                    ),
                ],
            ),
        )

    def on_login_click(self, _):
        print("Login link clicked")
        self.page.go("/login")
