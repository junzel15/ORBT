import flet as ft
import bcrypt
import re
import random
from pages.registration.components.customtextfield import CustomTextField
from pages.registration.components.country_code_selector import CountryPhoneCodeSelector
from pages.registration.components.country_data import load_country_data
import uuid
from dynamodb.dynamoDB_profiles import dynamo_write, dynamo_read


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

        self.page.window_width = 400
        self.page.window_height = 800
        self.page.update()

    def is_valid_email(self, email):
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None

    def is_email_unique(self, email):
        try:
            response = dynamo_read("profiles", "email", email)
            return response is None
        except Exception as e:
            print(f"Error reading DynamoDB: {e}")
            return False

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

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
        user_uuid = str(uuid.uuid4())

        user_data = {
            "email": email,
            "uuid": user_uuid,
            "full_name": full_name,
            "password": password_hashed,
            "phone_number": phone_number,
            "address": "Boston, U.S.A",
            "gender": "",
            "birthdate": "",
            "bio": "",
            "interests": [],
            "otp": otp,
            "verified": False,
            "profile_image": "",
        }

        dynamo_write("profiles", user_data)

        booking_data = {
            "uuid": user_uuid,
            "booking_id": "ORBT-BR0001",
            "date": "",
            "time": "",
            "location": "Boston, U.S.A",
            "event_name": "",
            "book_option_order": "",
            "status": "Upcoming",
            "venue_name": "Viga, 245-275 Washington St, Boston, MA 02108 ",
            "Coffee_image": "images/Coffee.png",
            "Brunch_image": "images/Brunch.png",
            "Diner_image": "images/Diner.png",
            "Dining_image": "images/Icon Dinning.png",
            "Bars_image": "images/Bars.png",
            "Experiences_image": "images/Experiences.png",
        }

        self.go_to("/verification", self.page, user_email=email)

        self.error_message.value = "Account created successfully! OTP sent."
        self.error_message.color = "green"
        self.error_message.visible = True
        self.page.update()

        self.go_to("/verification", self.page, user_email=email)

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
