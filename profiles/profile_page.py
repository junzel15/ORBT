import flet as ft
import json
from utils.data_provider import get_user_data


class ProfilePage:
    def __init__(self, page: ft.Page, go_to):
        self.page = page
        self.go_to = go_to

        self.page.title = "Profile"
        self.page.padding = 0
        self.page.scroll = "adaptive"
        self.page.bgcolor = "#F8F9FA"

        all_users = get_user_data()

        self.user_data = all_users[0] if all_users else {}

        user_profile_image = self.user_data.get("profile_image", None)

        self.profile_header = ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Row(
                                [
                                    ft.IconButton(
                                        icon=ft.Icons.ARROW_BACK,
                                        icon_size=24,
                                        bgcolor="transparent",
                                        on_click=lambda _: self.go_to(
                                            "/homepage", page
                                        ),
                                    ),
                                    ft.Text(
                                        value="Profile",
                                        size=18,
                                        weight="bold",
                                    ),
                                ],
                                alignment="start",
                                vertical_alignment="center",
                            ),
                            ft.IconButton(
                                icon=ft.Icons.MORE_VERT,
                                icon_size=24,
                                bgcolor="transparent",
                                on_click=lambda _: self.go_to(
                                    "/profile/settings", self.page
                                ),
                            ),
                        ],
                        alignment="spaceBetween",
                        vertical_alignment="center",
                    ),
                    ft.Container(
                        content=(
                            ft.Image(
                                src=user_profile_image if user_profile_image else "",
                                width=100,
                                height=100,
                                fit=ft.ImageFit.COVER,
                                border_radius=50,
                            )
                            if user_profile_image
                            else ft.CircleAvatar(
                                content=ft.Text(
                                    self.user_data.get("full_name", "N/A")[0],
                                    size=50,
                                    weight="bold",
                                    color="white",
                                ),
                                bgcolor="gray",
                                width=100,
                                height=100,
                            )
                        ),
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        content=ft.Text(
                            value=self.user_data.get("full_name", "N/A"),
                            size=20,
                            weight="bold",
                        ),
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        content=ft.Text(
                            value=self.user_data.get("address", "N/A"),
                            size=14,
                            color="gray",
                        ),
                        alignment=ft.alignment.center,
                    ),
                    ft.Row(
                        [
                            ft.Text("350 following", size=14, weight="bold"),
                            ft.Text("647 followers", size=14, weight="bold"),
                        ],
                        alignment="center",
                        spacing=20,
                    ),
                ],
                spacing=10,
                alignment="center",
            ),
            padding=15,
            alignment=ft.alignment.center,
        )

        self.bio_section = ft.Container(
            content=ft.Column(
                [
                    ft.Text("My Bio", size=16, weight="bold"),
                    ft.Row(
                        controls=[
                            ft.Text(
                                value=self.user_data.get("bio", "N/A"),
                                size=14,
                                color="gray",
                                overflow="ellipsis",
                                width=240,
                            ),
                            ft.TextButton(
                                "Read More",
                                on_click=lambda _: print("Read more clicked"),
                            ),
                        ],
                        alignment="start",
                        wrap=True,
                        spacing=10,
                    ),
                ],
                spacing=10,
            ),
            padding=15,
        )

        self.interest_section = ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("My Interests", size=16, weight="bold"),
                            ft.IconButton(icon=ft.icons.EDIT, icon_size=18),
                        ],
                        alignment="spaceBetween",
                    ),
                    ft.Row(
                        wrap=True,
                        spacing=10,
                        controls=[
                            ft.Container(
                                content=ft.Image(
                                    src="assets/images/Frame 18781.png",
                                    fit=ft.ImageFit.CONTAIN,
                                ),
                            ),
                            ft.Container(
                                content=ft.Image(
                                    src="assets/images/Frame 18782.png",
                                    fit=ft.ImageFit.CONTAIN,
                                ),
                            ),
                        ],
                    ),
                ],
                spacing=5,
            ),
            padding=15,
        )

        is_mobile = self.page.window_width < 600

        self.bottom_nav = ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        content=ft.Image(
                            src="assets/images/Home.png",
                            width=(24 if not is_mobile else 20),
                            height=(24 if not is_mobile else 20),
                        ),
                        on_click=lambda _: self.go_to("/homepage", self.page),
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src="assets/images/Star.png",
                            width=(24 if not is_mobile else 20),
                            height=(24 if not is_mobile else 20),
                        ),
                        on_click=lambda _: self.go_to("/bookings/upcoming", self.page),
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src="assets/images/Message.png",
                            width=(24 if not is_mobile else 20),
                            height=(24 if not is_mobile else 20),
                        ),
                        on_click=lambda _: self.go_to("/messages", self.page),
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src="assets/images/Profile.png",
                            width=(24 if not is_mobile else 20),
                            height=(24 if not is_mobile else 20),
                        ),
                        on_click=lambda _: self.go_to("/profile", self.page),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            bgcolor="#FFFFFF",
            border_radius=30,
        )

        self.main_content = ft.ListView(
            controls=[
                self.profile_header,
                self.bio_section,
                self.interest_section,
            ],
            expand=True,
            padding=ft.padding.all(16),
        )

    def render(self):
        return ft.Column(
            controls=[
                ft.Container(
                    content=self.main_content,
                    expand=True,
                ),
                self.bottom_nav,
            ],
            expand=True,
            spacing=0,
        )
