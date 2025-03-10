import flet as ft
from global_state import get_logged_in_user


class HomePage:

    def __init__(self, page: ft.Page, go_to, user):
        self.page = page
        self.go_to = go_to
        self.user = get_logged_in_user()
        self.user_name = self.user.get("full_name", "Guest") if self.user else "Guest"

        self.set_mobile_view()

        self.page.on_resize = self.adjust_window_size
        self.adjust_window_size()
        self.page.update()

    def set_mobile_view(self):
        self.page.window_width = 400
        self.page.window_height = 680

    def adjust_window_size(self, _=None):
        screen_width = self.page.window_width
        screen_height = self.page.window_height

        if screen_width <= 480:
            self.set_mobile_view()
        elif 481 <= screen_width <= 1024:
            self.page.window_width = min(screen_width, 800)
            self.page.window_height = min(screen_height, 1000)
        else:
            self.page.window_width = min(screen_width, 1200)
            self.page.window_height = min(screen_height, 900)

        self.page.update()

    def save_booking(self, event_name):
        user = get_logged_in_user()
        if not user:
            print("No user is logged in.")
            return

        if not event_name:
            print("⚠️ Warning: event_name is missing! Defaulting to 'Unknown'.")
            event_name = "Unknown"

        self.selected_event_name = event_name
        print(f"Event '{event_name}' saved successfully.")

    def on_option_click(self, event_name, route):
        print(f"on_option_click called with event_name: {event_name}, route: {route}")
        self.save_booking(event_name)
        self.go_to(route, self.page, kwargs={"event_name": event_name})

    def render(self):
        self.user = get_logged_in_user()
        self.user_name = self.user.get("full_name", "Guest") if self.user else "Guest"
        is_mobile = self.page.width < 600

        self.Header_Section = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Image(
                        src="images/Location.png",
                        width=24,
                        height=24,
                    ),
                    ft.Text(
                        "Add your location",
                        size=12 if is_mobile else 14,
                        style="Instrument Sans",
                        color="#747688",
                        expand=True,
                    ),
                    ft.Image(
                        src="images/Notify.png",
                        width=20,
                        height=20,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=ft.padding.symmetric(horizontal=16),
            margin=ft.margin.only(bottom=16),
        )

        self.Greeting_Description_Section = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                "Hello, ",
                                size=16,
                                style="Instrument Sans",
                                color="#000000",
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Text(
                                self.user_name,
                                size=16,
                                style="Instrument Sans",
                                color="#6D28D9",
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Text(
                        "Find your crowd",
                        size=20 if not is_mobile else 18,
                        style="Instrument Sans",
                        color="#000000",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Text(
                        "Share the moment",
                        size=20 if not is_mobile else 18,
                        style="Sora",
                        color=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=["#8547FF", "#000000"],
                        ),
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Text(
                        "Book now, meet 5 strangers,\nand let the fun find you.",
                        size=14,
                        style="Instrument Sans",
                        color="#4B4B4B",
                        text_align=ft.TextAlign.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
            padding=ft.padding.symmetric(horizontal=16),
            margin=ft.margin.only(bottom=24),
        )

        self.Image_Section = ft.Container(
            content=ft.Image(
                src="images/Homepage Graphics.png",
                width=self.page.width * 0.9,
                height=130,
                fit=ft.ImageFit.COVER,
            ),
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=8, bottom=25),
        )

        self.Options_Section = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Image(
                                    src="images/Icon Dinning.png",
                                    width=40,
                                    height=24,
                                    fit=ft.ImageFit.CONTAIN,
                                ),
                                ft.Text(
                                    "Dining",
                                    expand=1,
                                    size=18,
                                    style="Sora",
                                    color="#FFFFFF",
                                ),
                                ft.Icon(
                                    ft.icons.ARROW_FORWARD,
                                    color="white",
                                    size=20,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        padding=ft.padding.all(16),
                        border_radius=12,
                        on_click=lambda e: self.on_option_click("Dining", "/diner"),
                    ),
                    ft.Divider(height=1, color="#FFFFFF22"),
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Image(
                                    src="images/Icon Bars.png",
                                    width=40,
                                    height=24,
                                    fit=ft.ImageFit.CONTAIN,
                                ),
                                ft.Text(
                                    "Bars",
                                    size=18,
                                    style="Sora",
                                    color="#FFFFFF",
                                    expand=1,
                                ),
                                ft.Icon(
                                    ft.icons.ARROW_FORWARD,
                                    color="white",
                                    size=20,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        padding=ft.padding.all(16),
                        border_radius=12,
                        on_click=lambda e: self.on_option_click("Bars", "/bars"),
                    ),
                    ft.Divider(height=1, color="#FFFFFF22"),
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Image(
                                    src="images/Icon Experiences.png",
                                    width=40,
                                    height=24,
                                    fit=ft.ImageFit.CONTAIN,
                                ),
                                ft.Text(
                                    "Experiences",
                                    size=18,
                                    style="Sora",
                                    color="#FFFFFF",
                                    expand=1,
                                ),
                                ft.Icon(
                                    ft.icons.ARROW_FORWARD,
                                    color="white",
                                    size=20,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        padding=ft.padding.all(16),
                        border_radius=12,
                        on_click=lambda e: self.on_option_click(
                            "Experiences", "/experience"
                        ),
                    ),
                ],
                spacing=0,
                scroll="always",
            ),
            padding=ft.padding.symmetric(horizontal=16),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#1a1a1a", "#5300FA"],
            ),
            border_radius=12,
        )

        self.bottom_nav = ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        content=ft.Image(
                            src="images/Home.png",
                            width=24,
                            height=24,
                        ),
                        icon_size=24,
                        icon_color="#000000",
                        on_click=lambda _: self.go_to("/homepage", self.page),
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src="images/Star.png",
                            width=24,
                            height=24,
                        ),
                        icon_size=24,
                        icon_color="#000000",
                        on_click=lambda _: self.go_to("/bookings", self.page),
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src="images/Message.png",
                            width=24,
                            height=24,
                        ),
                        icon_size=24,
                        icon_color="#000000",
                        on_click=lambda _: self.go_to("/messages", self.page),
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src="images/Profile.png",
                            width=24,
                            height=24,
                        ),
                        icon_size=24,
                        icon_color="#000000",
                        on_click=lambda _: self.go_to("/profile", self.page),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            bgcolor="#FFFFFF",
            border_radius=30,
            padding=ft.padding.symmetric(vertical=10),
        )

        self.main_content = ft.ListView(
            controls=[
                self.Header_Section,
                self.Greeting_Description_Section,
            ],
            expand=True,
        )

        return ft.Column(
            controls=[
                ft.Container(
                    content=self.main_content,
                    expand=True,
                ),
                ft.Column(
                    controls=[
                        self.Image_Section,
                    ],
                    spacing=0,
                ),
                self.Options_Section,
                self.bottom_nav,
            ],
            expand=True,
            spacing=0,
        )
