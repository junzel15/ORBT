import flet as ft
import json
from utils.authenticate import authenticate_user
from utils.account_provider import get_user_data
from global_state import user_data


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
                height=42,
            ),
            alignment=ft.alignment.top_center,
            padding=ft.Padding(0, 40, 0, 20),
        )

        self.title_section = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    "Welcome Back",
                    font_family="Sora-SemiBold",
                    size=24,
                    height=31,
                    text_align=ft.TextAlign.CENTER,
                    color="#000000",
                    weight=ft.FontWeight.W_700,
                ),
            ],
        )

        self.email_field = ft.TextField(
            hint_text="Email",
            prefix_icon=ft.Icons.EMAIL,
            width=300,
        )
        self.password_field = ft.TextField(
            hint_text="Password",
            prefix_icon=ft.Icons.LOCK,
            suffix_icon=ft.Icons.VISIBILITY_OFF,
            password=True,
            width=300,
        )

        self.login_form_section = ft.Container(
            content=ft.Column(
                controls=[
                    self.email_field,
                    self.password_field,
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

        self.login_button_section = ft.Container(
            content=ft.ElevatedButton(
                text="Login",
                width=300,
                height=50,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                ),
                bgcolor="blue",
                color="white",
                on_click=self.login,
            ),
            padding=ft.Padding(0, 20, 0, 0),
        )

        self.forgot_password_section = ft.Row(
            controls=[
                ft.Text("Forgot your Password"),
                ft.TextButton(
                    "Reset password",
                    on_click=lambda _: print("Reset Password clicked"),
                    style=ft.ButtonStyle(
                        text_style=ft.TextStyle(
                            color="blue",
                            decoration=ft.TextDecoration.UNDERLINE,
                        )
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=0,
        )

        self.or_continue_with_section = ft.Row(
            controls=[
                ft.Divider(),
                ft.Text("Or continue with"),
                ft.Divider(),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.social_buttons_section = ft.Container(
            height=50,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                    ft.ElevatedButton(
                        expand=True,
                        content=ft.Row(
                            [
                                ft.Image(
                                    src="assets/images/icon_google.png",
                                    width=24,
                                    height=24,
                                    fit=ft.ImageFit.COVER,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        height=50,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                        ),
                        on_click=lambda _: print("Google sign-in"),
                    ),
                    ft.Container(width=20),
                    ft.ElevatedButton(
                        expand=True,
                        content=ft.Row(
                            [
                                ft.Image(
                                    src="assets/images/icon_fb.png",
                                    width=18,
                                    height=18,
                                    fit=ft.ImageFit.COVER,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        height=50,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                        ),
                        on_click=lambda _: print("Facebook sign-in"),
                    ),
                ],
            ),
        )

        self.footer_section = ft.Row(
            controls=[
                ft.Text("Don't have an account?"),
                ft.TextButton(
                    "Sign up",
                    on_click=lambda _: self.go_to("/registration", page),
                    style=ft.ButtonStyle(
                        text_style=ft.TextStyle(
                            color="#5300FA",
                            decoration=ft.TextDecoration.UNDERLINE,
                        )
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=0,
        )

        self.main_content = ft.Container(
            content=ft.Column(
                controls=[
                    self.header_section,
                    self.title_section,
                    self.login_form_section,
                    self.login_button_section,
                    self.forgot_password_section,
                    ft.Container(expand=True),
                    self.or_continue_with_section,
                    self.social_buttons_section,
                    self.footer_section,
                ],
                spacing=10,
            ),
            padding=ft.Padding(20, 0, 20, 0),
            bgcolor="transparent",
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
            self.show_snackbar_message("Please fill in all fields.")
            return

        user_data = authenticate_user(email, password)
        print(f"Authenticated user data: {user_data}")
        if user_data is None:
            self.show_snackbar_message("Authentication failed.")
            return

        user_data = get_user_data(email)
        print(f"User data from get_user_data: {user_data}")
        if user_data is None:
            self.show_snackbar_message("Error: User data not found.")
            return

        self.show_snackbar_message(f"Welcome, {user_data['full_name']}!")

        self.go_to("/homepage", self.page, user=user_data)

    def show_snackbar_message(self, message):
        """Display a snackbar with the provided message."""
        self.page.add(ft.SnackBar(content=ft.Text(message)))
        self.page.update()

    def render(self):
        return ft.Container(
            content=ft.Stack(
                expand=True,
                controls=[
                    ft.Image(
                        src="assets/images/registration_bg.png",
                        fit=ft.ImageFit.COVER,
                        expand=True,
                    ),
                    self.main_content,
                ],
            ),
            expand=True,
        )
