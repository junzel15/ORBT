import flet as ft
from datetime import datetime
import json


class DiningCoffeePage:

    def __init__(self, page: ft.Page, go_to, **kwargs):
        self.page = page
        self.go_to = go_to
        self.page.title = "Dining"
        self.page.theme_mode = None
        self.page.padding = 0
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.text_size = 12
        self.current_tab = "coffee"
        self.expanded_state = {"before": False, "expect": False}

        self.selected_date = kwargs.get("selected_date", "Default Date")

        self.dropdown_items = None
        self.date_dropdown = None

        self.selected_date = "Select a date"
        self.time_text_value = "10:00 AM"

        self.before_toggle_ref = ft.Ref[ft.Text]()
        self.expect_toggle_ref = ft.Ref[ft.Text]()
        self.before_content_ref = ft.Ref[ft.Container]()
        self.expect_content_ref = ft.Ref[ft.Container]()

        self.date_text = ft.Text(self.selected_date, size=14, color="white")

        self.time_text = ft.Text(self.time_text_value, size=14, color="white")

        self.page.on_resize = self.on_resize

        self.bookings = self.load_booking_data()

    def on_resize(self, e):
        pass

    def go_back(self):
        if len(self.page.views) > 1:
            self.page.views.pop()
            self.page.go(self.page.views[-1].route)
        else:
            self.page.go("/homepage")
        self.page.update()

    def render(self):
        self.page.on_resize = self.on_resize

    def change_tab(self, tab_name: str):
        self.current_tab = tab_name
        routes = {
            "coffee": "/coffee",
            "brunch": "/brunch",
            "diner": "/diner",
        }

        route = routes.get(tab_name)
        if route:
            self.page.go(route)
        else:
            print(f"Tab {tab_name} does not exist.")
        self.page.update()

    def toggle_tile(self, tile):
        self.expanded_state[tile] = not self.expanded_state[tile]
        toggle_ref = (
            self.before_toggle_ref if tile == "before" else self.expect_toggle_ref
        )
        content_ref = (
            self.before_content_ref if tile == "before" else self.expect_content_ref
        )

        toggle_ref.current.value = "-" if self.expanded_state[tile] else "+"
        content_ref.current.visible = self.expanded_state[tile]

        toggle_ref.current.update()
        content_ref.current.update()
        self.page.update()

    def render(self):
        self.page.on_resize = self.on_resize

    def load_booking_data(self):
        """Load booking data from JSON."""
        try:
            with open("booking.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def select_date(self, e, date_str):
        """Update selected date & time from JSON data."""
        try:

            formatted_date = datetime.strptime(date_str, "%A, %B %d").strftime(
                "%A, %B %d"
            )

            matching_bookings = [
                b for b in self.bookings if b["select_a_date"] == formatted_date
            ]

            if matching_bookings:

                self.selected_date = formatted_date
                self.selected_time = matching_bookings[0]["time"]

                self.date_text.value = self.selected_date
                self.time_text.value = self.selected_time

                self.dropdown_items.visible = False
                self.date_dropdown.content = ft.Row(
                    controls=[
                        self.date_text,
                        ft.Icon(name=ft.icons.ARROW_DROP_DOWN, color="white", size=16),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                )

                self.date_text.update()
                self.time_text.update()
                self.dropdown_items.update()
                self.page.update()
            else:
                print(f"No bookings found for {formatted_date}")
        except ValueError as ex:
            print(f"Error parsing date: {date_str} - {ex}")

    def toggle_dropdown(self, e):
        """Toggle the visibility of the date dropdown."""
        self.dropdown_items.visible = not self.dropdown_items.visible
        self.dropdown_items.update()
        self.page.update()

    def render(self):
        self.page.on_resize = self.on_resize
        date_list = list(set(b["select_a_date"] for b in self.bookings))

        header = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Image(
                                src="assets/images/Icon Dinning.png",
                                width=70,
                                height=50,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Text(
                                "Dining",
                                size=22,
                                color="white",
                                weight=ft.FontWeight.BOLD,
                            ),
                        ],
                        spacing=10,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),
                ft.Container(expand=True),
                ft.IconButton(
                    icon=ft.icons.CLOSE,
                    icon_color="white",
                    icon_size=22,
                    on_click=lambda e: self.go_back(),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        def create_tab_button(tab_name):
            return ft.TextButton(
                text=tab_name.capitalize(),
                on_click=lambda e: self.change_tab(tab_name),
                style=ft.ButtonStyle(
                    bgcolor=(
                        ft.colors.WHITE
                        if self.current_tab == tab_name
                        else ft.colors.TRANSPARENT
                    ),
                    shape=ft.RoundedRectangleBorder(radius=25),
                    side=ft.BorderSide(2, ft.colors.WHITE),
                    padding=ft.padding.symmetric(horizontal=20, vertical=8),
                    text_style=ft.TextStyle(
                        font_family="Instrument Sans",
                        size=14,
                        weight=ft.FontWeight.BOLD,
                        color=(
                            ft.colors.BLACK if tab_name == "coffee" else ft.colors.WHITE
                        ),
                    ),
                ),
            )

        tab_section = ft.Row(
            controls=[
                create_tab_button("coffee"),
                create_tab_button("brunch"),
                create_tab_button("diner"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=12,
        )

        self.dropdown_items = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Text(date, size=14, color="#FFFFFF"),
                        padding=8,
                        bgcolor=ft.colors.with_opacity(0.1, ft.colors.BLACK),
                        border_radius=4,
                        on_click=lambda e, date=date: self.select_date(e, date),
                    )
                    for date in date_list
                ],
                spacing=4,
            ),
            padding=8,
            bgcolor="#1A1A1A",
            border_radius=8,
            width=350,
            visible=False,
        )

        self.date_dropdown = ft.Container(
            content=ft.Row(
                controls=[
                    self.date_text,
                    ft.Icon(name=ft.icons.ARROW_DROP_DOWN, color="white", size=16),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=12,
            border=ft.border.all(color="white", width=1),
            border_radius=8,
            on_click=self.toggle_dropdown,
        )

        def create_section(title, tile_key, contents):
            toggle_ref = (
                self.before_toggle_ref
                if tile_key == "before"
                else self.expect_toggle_ref
            )
            content_ref = (
                self.before_content_ref
                if tile_key == "before"
                else self.expect_content_ref
            )

            return ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Text(
                                    title,
                                    color="white",
                                    size=14,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Container(
                                    content=ft.Text(
                                        "+", ref=toggle_ref, color="white", size=20
                                    ),
                                    on_click=lambda e: self.toggle_tile(tile_key),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Container(
                            content=ft.Column(controls=contents, spacing=8),
                            visible=False,
                            padding=ft.padding.only(top=8),
                            ref=content_ref,
                        ),
                    ],
                ),
                padding=ft.padding.all(16),
            )

        def create_underlined_text(main_text, sub_text, style):
            return ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            main_text,
                            color="white",
                            size=self.text_size,
                            weight=ft.FontWeight.BOLD,
                        ),
                        border=ft.border.only(bottom=ft.BorderSide(1, "white")),
                        padding=ft.padding.only(bottom=2),
                    ),
                    ft.Text(sub_text, color="#999BFF", size=self.text_size),
                ],
                spacing=2,
            )

        before_you_book = create_section(
            "BEFORE YOU BOOK",
            "before",
            [
                create_underlined_text(
                    "Free to Reserve",
                    "You only pay for what you order at the table.",
                    style=ft.TextStyle(font_family="Instrument Sans", size=12),
                ),
                create_underlined_text(
                    "Be Ready",
                    "Your group is counting on you, so only book if you’re sure to join!",
                    style=ft.TextStyle(font_family="Instrument Sans", size=12),
                ),
            ],
        )

        what_to_expect = create_section(
            "WHAT TO EXPECT",
            "expect",
            [
                create_underlined_text(
                    "Meet Your Crew",
                    "5 strangers with shared vibes and fun personalities.",
                    style=ft.TextStyle(font_family="Instrument Sans", size=12),
                ),
                create_underlined_text(
                    "Relax & Connect",
                    "Great food, better conversations, and easy icebreakers.",
                    style=ft.TextStyle(font_family="Instrument Sans", size=12),
                ),
            ],
        )

        event_details = ft.Container(
            content=ft.ResponsiveRow(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Image(
                                            src="assets/images/Group.png",
                                            width=50,
                                            height=50,
                                        ),
                                        padding=ft.padding.only(right=10),
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Container(
                                                content=ft.Text(
                                                    "Event details—like the restaurant, table, and hints about your group—will be revealed ",
                                                    size=12,
                                                    font_family="Instruments Sans",
                                                    max_lines=None,
                                                    selectable=True,
                                                    text_align=ft.TextAlign.LEFT,
                                                    color="#FFFFFF",
                                                ),
                                                width=200,
                                            ),
                                            ft.Container(
                                                content=ft.Row(
                                                    controls=[
                                                        ft.Text(
                                                            "1 day",
                                                            size=12,
                                                            font_family="Instruments Sans",
                                                            weight=ft.FontWeight.BOLD,
                                                            color="#999BFF",
                                                        ),
                                                        ft.Text(
                                                            " before.",
                                                            size=12,
                                                            font_family="Instruments Sans",
                                                            color="#FFFFFF",
                                                        ),
                                                    ],
                                                    alignment=ft.MainAxisAlignment.START,
                                                ),
                                                width=200,
                                            ),
                                        ],
                                        spacing=2,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START,
                                wrap=True,
                            )
                        ],
                        expand=True,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=ft.padding.all(10),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.with_opacity(0.1, ft.colors.BLACK),
            border_radius=10,
            width=self.page.width * 0.95,
        )

        book_now_button = ft.Container(
            content=ft.ElevatedButton(
                text="Book Now",
                on_click=lambda e: self.go_to("/loadingscreen", self.page),
                style=ft.ButtonStyle(
                    bgcolor={
                        ft.MaterialState.DEFAULT: "#A2A8BF",
                        ft.MaterialState.HOVERED: ft.colors.BLUE,
                    },
                    color="#FFFFFF",
                    padding=ft.padding.symmetric(horizontal=20, vertical=10),
                    text_style=ft.TextStyle(
                        font_family="Intruments Sans",
                        size=16,
                    ),
                ),
                width=200,
                height=45,
            ),
            alignment=ft.alignment.center,
            padding=ft.padding.only(top=16, bottom=32),
        )

        background = ft.Container(
            content=ft.Image(
                src="assets/images/Dark Background 2 Screen.png",
                fit=ft.ImageFit.COVER,
            ),
            width=self.page.window_width,
            height=self.page.window_height,
            alignment=ft.alignment.center,
        )

        main_content = ft.Container(
            content=ft.Column(
                controls=[
                    header,
                    tab_section,
                    self.date_dropdown,
                    self.dropdown_items,
                    before_you_book,
                    what_to_expect,
                    event_details,
                    book_now_button,
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO,
            ),
            expand=True,
            padding=ft.padding.all(16),
        )

        return ft.View(
            route="/coffee",
            controls=[
                ft.Stack(
                    controls=[background, main_content],
                    expand=True,
                )
            ],
        )
