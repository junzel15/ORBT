import flet as ft


class ProfileSettingsPage:
    def __init__(self, page: ft.Page, go_to):
        self.page = page
        self.go_to = go_to

        self.page.title = "Settings"
        self.page.padding = 0
        self.page.scroll = "adaptive"
        self.page.bgcolor = "#F8F9FA"

        self.main_content = None
        self.build_ui()

    def build_ui(self):
        def create_list_item(icon_name, text, trailing=None, on_click=None):
            return ft.Container(
                content=ft.Row(
                    [
                        ft.Row(
                            [
                                ft.Icon(icon_name, size=24, color="#000000"),
                                ft.Text(
                                    text, size=16, weight="normal", color="#000000"
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        ft.Container(
                            content=(
                                trailing
                                if trailing
                                else ft.Icon(
                                    ft.icons.CHEVRON_RIGHT, size=24, color="#6c757d"
                                )
                            ),
                            alignment=ft.alignment.center_right,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                padding=ft.padding.symmetric(horizontal=10, vertical=15),
                height=50,
                ink=True,
                on_click=on_click,
            )

        header = ft.Container(
            content=ft.Row(
                [
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        icon_size=24,
                        on_click=lambda e: self.go_to("/profile"),
                    ),
                    ft.Text("Settings", size=20, weight="bold", color="#000000"),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
            padding=ft.padding.symmetric(horizontal=10, vertical=15),
            height=60,
            bgcolor="#FFFFFF",
        )

        items = [
            create_list_item(
                ft.icons.EDIT,
                "Edit Profile",
                on_click=lambda e: self.go_to("/profile/edit"),
            ),
            create_list_item(ft.icons.BLOCK, "Blocked"),
            create_list_item(
                ft.icons.NOTIFICATIONS,
                "Notifications",
                trailing=ft.Switch(value=True, active_color="blue"),
            ),
            create_list_item(ft.icons.LOCK, "Change Password"),
            create_list_item(ft.icons.PAYMENT, "Payments"),
            create_list_item(
                ft.icons.LANGUAGE,
                "Language",
                trailing=ft.Text("English (US)", size=14, color="#6c757d"),
            ),
            create_list_item(ft.icons.SECURITY, "Account & Security"),
            create_list_item(ft.icons.HELP, "Help Centre"),
            create_list_item(ft.icons.STAR, "Rate Us"),
        ]

        self.logout_item = ft.Container(
            content=ft.Row(
                [
                    ft.Icon(ft.icons.LOGOUT, size=24, color="red"),
                    ft.Text("Log Out", size=16, weight="normal", color="red"),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            padding=ft.padding.symmetric(horizontal=10, vertical=15),
            height=50,
            ink=True,
        )

        self.main_content = items

    def render(self):
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Row(
                        [
                            ft.IconButton(
                                icon=ft.icons.ARROW_BACK,
                                icon_size=24,
                                on_click=lambda e: self.go_to("/profile"),
                            ),
                            ft.Text(
                                "Settings", size=20, weight="bold", color="#000000"
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10,
                    ),
                    padding=ft.padding.symmetric(horizontal=10, vertical=15),
                    height=60,
                    bgcolor="#FFFFFF",
                ),
                ft.Container(
                    content=ft.ListView(
                        controls=self.main_content,
                        spacing=10,
                        padding=10,
                        expand=True,
                    ),
                    expand=True,
                ),
                ft.Container(
                    content=self.logout_item,
                    padding=ft.padding.symmetric(vertical=10, horizontal=10),
                ),
            ],
            expand=True,
        )
