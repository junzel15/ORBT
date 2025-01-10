import flet as ft
from registration.components.form_filled import form_filled


def RegistrationPage(page, go_to):
    def register_user(e):

        print("User registered!")

    return ft.View(
        "/registration",
        controls=[
            ft.Container(
                expand=True,
                bgcolor="white",
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Image(
                                src="assets/images/ORBT Logo - Splash Screen.png",
                                fit=ft.ImageFit.CONTAIN,
                                height=50,
                            ),
                            alignment=ft.alignment.top_center,
                            padding=ft.padding.only(top=20),
                        ),
                        ft.Container(
                            content=ft.Text(
                                "Create an Account",
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                color="black",
                            ),
                            alignment=ft.alignment.top_center,
                            padding=ft.padding.only(top=10),
                        ),
                        ft.Container(
                            content=ft.Text(
                                "Fill your information below or register with\n"
                                "your social account.",
                                size=14,
                                color="gray",
                                text_align=ft.TextAlign.CENTER,
                            ),
                            alignment=ft.alignment.top_center,
                            padding=ft.padding.only(top=5, bottom=20),
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    form_filled(
                                        "Full Name",
                                        "Enter your full name",
                                        icon=ft.icons.PERSON,
                                    ),
                                    form_filled(
                                        "Email Address",
                                        "Enter your email",
                                        icon=ft.icons.EMAIL,
                                    ),
                                    form_filled(
                                        "Password",
                                        "Enter your password",
                                        is_password=True,
                                        icon=ft.icons.LOCK,
                                    ),
                                    form_filled(
                                        "Phone Number",
                                        "+63",
                                        icon=ft.icons.PHONE,
                                    ),
                                    ft.Checkbox(label="Agree with Terms & Conditions"),
                                ],
                                spacing=15,
                            ),
                            padding=ft.padding.symmetric(horizontal=20),
                        ),
                        ft.Container(
                            content=ft.ElevatedButton(
                                "Register",
                                on_click=register_user,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=10),
                                    padding=ft.padding.symmetric(
                                        vertical=12, horizontal=20
                                    ),
                                ),
                            ),
                            alignment=ft.alignment.center,
                            padding=ft.padding.only(top=10, bottom=20),
                        ),
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.ElevatedButton(
                                        text="Google",
                                        icon=ft.icons.ACCOUNT_CIRCLE,
                                        on_click=lambda _: print("Google sign-in"),
                                    ),
                                    ft.ElevatedButton(
                                        text="Facebook",
                                        icon=ft.icons.GROUP,
                                        on_click=lambda _: print("Facebook sign-in"),
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=15,
                            ),
                        ),
                        ft.Container(
                            content=ft.TextButton(
                                "Already have an account? Log in",
                                on_click=lambda _: go_to("/login"),
                            ),
                            alignment=ft.alignment.center,
                            padding=ft.padding.only(top=20),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    expand=True,
                ),
            )
        ],
    )
