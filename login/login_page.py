import flet as ft
import json
from utils import authenticate_user


class LoginPage:
    def __init__(self, page, go_to):
        self.page = page
        self.go_to = go_to

        self.users = self.load_users()
        self.logged_in_user = None

        self.header_section = ft.Container(
            content=ft.Image(
                src="assets/images/logo_blue.png",
                fit=ft.ImageFit.CONTAIN,
                height=50,
            ),
            alignment=ft.alignment.top_center,
            padding=ft.padding.only(top=20),
        )

        self.title_section = ft.Container(
            content=ft.Text(
                "Welcome Back",
                size=24,
                style="Sora",
                weight=ft.FontWeight.BOLD,
                color="black",
            ),
            alignment=ft.alignment.top_center,
            padding=ft.padding.only(top=10),
        )

        self.email_field = ft.TextField(
            label="Email",
            hint_text="Enter your email",
            keyboard_type=ft.KeyboardType.EMAIL,
            autofocus=True,
            border_color="gray",
            width=300,
            text_style=ft.TextStyle(font_family="Instrument Sans", size=14),
        )
        self.password_field = ft.TextField(
            label="Password",
            hint_text="Enter your password",
            password=True,
            border_color="gray",
            width=300,
            text_style=ft.TextStyle(font_family="Instrument Sans", size=14),
        )

        self.login_form_section = ft.Container(
            content=ft.Column(
                controls=[self.email_field, self.password_field],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
            padding=ft.padding.only(top=20),
        )

        self.login_button_section = ft.Container(
            content=ft.ElevatedButton(
                text="Login",
                width=300,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=8),
                    bgcolor="blue",
                    color="white",
                    padding=ft.padding.symmetric(vertical=12),
                    text_style=ft.TextStyle(font_family="Instrument Sans", size=16),
                ),
                on_click=self.login,
            ),
            alignment=ft.alignment.center,
            padding=ft.padding.only(top=20),
        )

        self.forgot_password_section = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text(
                        "Forgot your password?",
                        size=12,
                        color="gray",
                        style=ft.TextStyle(
                            font_family="Instrument Sans",
                        ),
                    ),
                    ft.TextButton(
                        "Reset Password",
                        on_click=lambda _: print("Reset Password clicked"),
                        style=ft.ButtonStyle(
                            color="blue",
                            text_style=ft.TextStyle(
                                font_family="Instrument Sans", size=12
                            ),
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=ft.padding.only(top=10),
        )

        self.or_continue_with_section = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Divider(thickness=1, color="gray"),
                        expand=True,
                    ),
                    ft.Text(
                        "Or continue with",
                        size=14,
                        color="gray",
                        style=ft.TextStyle(
                            font_family="Instrument Sans",
                        ),
                    ),
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
                    ft.Text(
                        "Don't have an account?",
                        size=14,
                        color="gray",
                        style=ft.TextStyle(
                            font_family="Instrument Sans",
                        ),
                    ),
                    ft.TextButton(
                        "Sign up",
                        on_click=lambda _: self.go_to("/registration", page),
                        style=ft.ButtonStyle(
                            color="blue",
                            text_style=ft.TextStyle(
                                font_family="Instrument Sans",
                                size=14,
                                weight=ft.FontWeight.BOLD,
                            ),
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
                    self.login_form_section,
                    self.login_button_section,
                    self.forgot_password_section,
                ],
                expand=True,
            ),
            alignment=ft.alignment.center,
            border_radius=15,
            padding=ft.padding.all(20),
        )

    def load_users(self):
        try:
            with open("users.json", "r") as file:
                return json.load(file)
        except Exception as e:
            print(f"Error loading users.json: {e}")
            return []

    def login(self, _):
        email = self.email_field.value.strip()
        password = self.password_field.value.strip()

        if not email or not password:
            self.page.snack_bar = ft.SnackBar(ft.Text("Please fill in all fields."))
            self.page.snack_bar.open = True
            self.page.update()
            return

        user_data = authenticate_user(email, password)

        if user_data:
            self.page.snack_bar = ft.SnackBar(
                ft.Text(f"Welcome, {user_data['full_name']}!")
            )
            self.page.snack_bar.open = True
            self.page.update()

            self.go_to(
                "/homepage",
                self.page,
                user_name=user_data["full_name"],
                address=user_data["address"],
                bio=user_data["bio"],
            )
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Invalid email or password."))
            self.page.snack_bar.open = True
            self.page.update()

    def render(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.ListView(
                        controls=[
                            self.header_section,
                            self.title_section,
                            self.login_form_section,
                            self.login_button_section,
                            self.forgot_password_section,
                        ],
                        expand=True,
                    ),
                    self.or_continue_with_section,
                    self.social_buttons_section,
                    self.footer_section,
                ]
            ),
            expand=True,
            image_src="assets/images/registration_bg.png",
            image_fit=ft.ImageFit.COVER,
        )
