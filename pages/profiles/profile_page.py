import flet as ft
from global_state import get_logged_in_user
import boto3
from botocore.exceptions import ClientError


class ProfilePage:
    def __init__(self, page: ft.Page, go_to, user=None):
        self.page = page
        self.go_to = go_to
        self.user = user if user is not None else get_logged_in_user()

        self.user_name = self.user.get("full_name", "Guest")
        self.user_address = self.user.get("address") or "N/A"
        self.user_bio = self.user.get("bio", "N/A")
        self.user_profile_image = self.user.get("profile_image", None)

        self.page.title = "Profile"
        self.page.padding = 0
        self.page.scroll = "adaptive"
        self.page.bgcolor = "#F8F9FA"

        self.page.window_width = 400
        self.page.window_height = 680
        self.page.update()

    def render(self):
        self.user = get_logged_in_user() or {}
        self.user_name = self.user.get("full_name", "Guest")
        self.user_address = self.user.get("address") or "N/A"
        self.user_bio = self.user.get("bio", "N/A")
        profile_image = self.user.get("profile_image", None)
        is_mobile = self.page.window_width < 600

        profile_header = ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.IconButton(
                                icon=ft.icons.ARROW_BACK,
                                icon_size=24,
                                bgcolor="transparent",
                                on_click=lambda _: self.go_to("/homepage", self.page),
                            ),
                            ft.Text("Profile", size=18, weight="bold"),
                            ft.IconButton(
                                icon=ft.icons.MORE_VERT,
                                icon_size=24,
                                bgcolor="transparent",
                                on_click=lambda _: self.go_to("/settings", self.page),
                            ),
                        ],
                        alignment="spaceBetween",
                        vertical_alignment="center",
                    ),
                    ft.Container(
                        content=ft.Stack(
                            [
                                ft.CircleAvatar(
                                    radius=50,
                                    bgcolor="gray",
                                    content=(
                                        ft.Text(
                                            (
                                                self.user_name[0]
                                                if self.user_name
                                                else "?"
                                            ),
                                            size=50,
                                            weight="bold",
                                            color="white",
                                        )
                                        if not profile_image
                                        else ft.Container(
                                            content=ft.Image(
                                                src=profile_image,
                                                width=100,
                                                height=100,
                                                fit=ft.ImageFit.COVER,
                                            ),
                                            alignment=ft.alignment.center,
                                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                            border_radius=ft.border_radius.all(50),
                                        )
                                    ),
                                ),
                            ],
                            alignment=ft.alignment.center,
                        ),
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        content=ft.Text(self.user_name, size=20, weight="bold"),
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        content=ft.Text(self.user_address, size=14, color="gray"),
                        alignment=ft.alignment.center,
                    ),
                    ft.Row(
                        [
                            ft.Text(
                                f"{self.get_following_count()} following",
                                size=14,
                                weight="bold",
                            ),
                            ft.Text(
                                f"{self.get_followers_count()} followers",
                                size=14,
                                weight="bold",
                            ),
                        ],
                        alignment="center",
                        spacing=20,
                    ),
                ],
                spacing=10,
                alignment="center",
            ),
            padding=15,
        )

        bio_section = ft.Container(
            content=ft.Column(
                [
                    ft.Text("My Bio", size=16, weight="bold"),
                    ft.Column(
                        controls=[
                            ft.Text(
                                value=self.user_bio,
                                size=14,
                                color="gray",
                                max_lines=3,
                                selectable=True,
                            ),
                            ft.TextButton(
                                "Read More",
                                on_click=lambda _: print("Expand bio"),
                            ),
                        ],
                        spacing=5,
                    ),
                ],
                spacing=10,
            ),
            padding=15,
        )

        interest_section = ft.Container(
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
                    ),
                ],
                spacing=5,
            ),
            padding=15,
        )

        self.bottom_nav = ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        content=ft.Image(
                            src="images/Home.png",
                            width=(24 if not is_mobile else 20),
                            height=(24 if not is_mobile else 20),
                        ),
                        on_click=lambda _: self.go_to("/homepage", self.page),
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src="images/Star.png",
                            width=(24 if not is_mobile else 20),
                            height=(24 if not is_mobile else 20),
                        ),
                        on_click=lambda _: self.go_to("/bookings", self.page),
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src="images/Message.png",
                            width=(24 if not is_mobile else 20),
                            height=(24 if not is_mobile else 20),
                        ),
                        on_click=lambda _: self.go_to("/messages", self.page),
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src="images/Profile.png",
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

        main_content = ft.ListView(
            controls=[
                profile_header,
                bio_section,
                interest_section,
            ],
            expand=True,
            padding=ft.padding.all(16),
        )

        return ft.Column(
            controls=[
                ft.Container(content=main_content, expand=True),
                self.bottom_nav,
            ],
            expand=True,
            spacing=0,
        )

    def get_following_count(self):
        return len(self.user.get("friends", []))

    def get_followers_count(self):
        dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
        table = dynamodb.Table("profiles")

        try:
            response = table.scan(
                FilterExpression=boto3.dynamodb.conditions.Attr("friends").contains(
                    self.user["email"]
                )
            )
            return len(response.get("Items", []))
        except ClientError as e:
            print("Error scanning DynamoDB:", e)
            return 0
