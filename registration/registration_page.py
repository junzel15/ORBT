import flet as ft
import json
import re
import bcrypt


class RegistrationPage:
    def __init__(self, page, go_to):
        self.page = page
        self.go_to = go_to

        self.error_message = ft.Text(visible=False)

        self.header_section = ft.Container(
            content=ft.Image(
                src="assets/images/logo_blue.png",
                fit=ft.ImageFit.CONTAIN,
                height=50,
            ),
            alignment=ft.alignment.top_center,
            padding=ft.padding.only(top=20),
        )

        self.full_name_input = ft.TextField(label="Full Name", autofocus=True)
        self.email_input = ft.TextField(label="Email")
        self.password_input = ft.TextField(label="Password", password=True)

        self.phone_input = ft.Ref[ft.TextField]()

        self.title_section = ft.Container(
            content=ft.Text(
                "Create an Account",
                size=24,
                weight=ft.FontWeight.BOLD,
                color="black",
            ),
            alignment=ft.alignment.top_center,
            padding=ft.padding.only(top=10),
        )

        self.description_section = ft.Container(
            content=ft.Text(
                "Fill your information below or register with your social account.",
                size=14,
                color="gray",
                text_align=ft.TextAlign.CENTER,
            ),
            alignment=ft.alignment.top_center,
            padding=ft.padding.only(top=5, bottom=20),
        )

        self.form_section = ft.Container(
            content=ft.Column(
                controls=[
                    self.full_name_input,
                    self.email_input,
                    self.password_input,
                    ft.Row(
                        controls=[
                            ft.Dropdown(
                                width=80,
                                options=[
                                    ft.dropdown.Option("PH", text="🇵🇭"),
                                    ft.dropdown.Option("US", text="🇺🇸"),
                                    ft.dropdown.Option("IN", text="🇮🇳"),
                                    ft.dropdown.Option("CN", text="🇨🇳"),
                                    ft.dropdown.Option("JP", text="🇯🇵"),
                                ],
                                value="PH",
                                on_change=lambda e: self.update_phone_code(
                                    e.control.value
                                ),
                            ),
                            ft.TextField(
                                ref=self.phone_input,
                                label=None,
                                hint_text="Phone Number",
                                text_style=ft.TextStyle(color="lightgray"),
                                keyboard_type=ft.KeyboardType.NUMBER,
                            ),
                        ],
                        spacing=5,
                    ),
                    ft.Checkbox(
                        label="Agree with Terms & Condition",
                        width=300,
                    ),
                ],
                spacing=15,
            ),
            alignment=ft.alignment.top_center,
            padding=ft.padding.symmetric(horizontal=20),
        )

        self.register_button_section = ft.ElevatedButton(
            "Register",
            on_click=self.register_user,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=30),
                padding=ft.padding.symmetric(vertical=20, horizontal=0),
                bgcolor="#d1d5db",
                color="black",
                elevation=0,
            ),
            width=300,
            height=50,
        )

        self.verification_message = ft.Text(
            "Registration successful! Please verify your email.",
            size=20,
            color="green",
            visible=False,
        )

        self.or_continue_with_section = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Divider(thickness=1, color="gray"),
                        expand=True,
                    ),
                    ft.Text("Or continue with", size=12, color="gray"),
                    ft.Container(
                        content=ft.Divider(thickness=1, color="gray"),
                        expand=True,
                    ),
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=ft.padding.only(top=10, bottom=10),
        )

        self.social_buttons_section = ft.Row(
            controls=[
                ft.ElevatedButton(
                    content=ft.Row(
                        controls=[
                            ft.Image(
                                src="assets/images/icon_google.png",
                                width=100,
                                height=20,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=8,
                    ),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                        bgcolor="white",
                        color="black",
                        padding=ft.padding.symmetric(vertical=12, horizontal=16),
                    ),
                    on_click=lambda _: print("Google sign-in"),
                ),
                ft.ElevatedButton(
                    content=ft.Row(
                        controls=[
                            ft.Image(
                                src="assets/images/icon_fb.png",
                                width=100,
                                height=20,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=8,
                    ),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                        bgcolor="white",
                        color="black",
                        padding=ft.padding.symmetric(vertical=12, horizontal=16),
                    ),
                    on_click=lambda _: print("Facebook sign-in"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        )

        self.footer_section = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text("Already have an account?", size=12, color="gray"),
                    ft.TextButton(
                        "Log in",
                        on_click=lambda _: self.go_to("/login"),
                        style=ft.ButtonStyle(
                            color="blue",
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=ft.padding.only(top=20),
        )

        self.main_content = ft.Container(
            content=ft.ListView(
                controls=[
                    self.header_section,
                    self.title_section,
                    self.description_section,
                    self.form_section,
                    self.register_button_section,
                    self.or_continue_with_section,
                    self.social_buttons_section,
                    self.footer_section,
                ],
                expand=True,
            ),
            alignment=ft.alignment.center,
            border_radius=15,
            padding=ft.padding.all(20),
        )

    def update_phone_code(self, country_code):
        """Update phone code based on selected country."""
        phone_codes = {
            "PH": "+63",
            "US": "+1",
            "IN": "+91",
            "CN": "+86",
            "JP": "+81",
        }
        if country_code in phone_codes:
            self.phone_input.current.value = phone_codes[country_code]
            self.page.update()

    def is_valid_email(self, email):
        """Validate email format."""
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None

    def is_email_unique(self, email):
        """Check if the email is already registered."""
        try:
            with open("users.json", "r") as file:
                users = json.load(file)
                return not any(user["email"] == email for user in users)
        except FileNotFoundError:
            return True

    def hash_password(self, password):
        """Hash the password securely."""
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def save_user_to_json(self, user_data):
        """Save the user data to the users.json file."""
        try:
            with open("users.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.append(user_data)

        with open("users.json", "w") as file:
            json.dump(data, file, indent=4)

    def register_user(self, e):

        full_name = self.full_name_input.value.strip()
        email = self.email_input.value
        password = self.password_input.value
        phone_number = self.phone_input.current.value

        print("Full Name:", full_name)
        print("Email:", email)
        print("Password:", password)
        print("Phone Number:", phone_number)

        if not full_name or not email or not password or not phone_number:
            print("Validation failed: Some fields are empty.")
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

        password = self.hash_password(password)

        self.save_user_to_json(
            {
                "full_name": full_name,
                "email": email,
                "password": password,
                "phone_number": phone_number,
            }
        )

        self.error_message.value = "Account created successfully!"
        self.error_message.color = "green"
        self.error_message.visible = True
        self.page.update()

    def render(self):
        return ft.Container(
            content=self.main_content,
            expand=True,
            image_src="assets/images/registration_bg.png",
            image_fit=ft.ImageFit.COVER,
        )
