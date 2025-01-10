import flet as ft
from flet import TextStyle, FontWeight


class BarsPage:
    def __init__(self, page: ft.Page, go_to):
        # Page and navigation setup
        self.page = page
        self.go_to = go_to
        self.page.title = "Bars"
        self.page.theme_mode = None
        self.page.padding = 0
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.text_size = 12
        self.expanded_state = {"before": False, "expect": False}

        # References for toggle and content sections
        self.before_toggle_ref = ft.Ref[ft.Text]()
        self.expect_toggle_ref = ft.Ref[ft.Text]()
        self.before_content_ref = ft.Ref[ft.Container]()
        self.expect_content_ref = ft.Ref[ft.Container]()

    def on_resize(self, e):
        pass  # Prevents the AttributeError

    def render(self):
        self.page.on_resize = self.on_resize  # Attach resize handler

    def toggle_tile(self, tile):
        """Toggle the visibility of a content tile."""
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

    def book_now(self, e):
        """Handle the Book Now button click."""
        print("Booking now...")
        self.go_to("/")

    def render(self):
        """Render the main content of the page."""
        self.page.on_resize = self.on_resize

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

        background = ft.Container(
            content=ft.Image(
                src="assets/images/Dark Background 2 Screen.png",
                fit=ft.ImageFit.COVER,
            ),
            width=400,
            height=900,
            alignment=ft.alignment.center,
        )

        # Header
        header = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Image(
                                src="assets/images/Icon Bars.png",
                                width=70,
                                height=50,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Text(
                                "Bars",
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
                    on_click=lambda e: (
                        self.page.views.pop(),
                        self.page.go("/booking"),
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        def toggle_dropdown(e):
            dropdown_items.visible = not dropdown_items.visible
            dropdown_items.update()

        dropdown_items = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            "Thursday, March 14",
                                            size=14,
                                            font_family="Instruments Sans",
                                            weight=ft.FontWeight.BOLD,
                                            color="#FFFFFF",
                                        ),
                                        ft.Icon(
                                            name=ft.icons.STAR,
                                            color="#FFD700",
                                            size=16,
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                                ft.Text(
                                    "10:00 AM",
                                    size=12,
                                    font_family="Instruments Sans",
                                    color="#FFFFFF",
                                ),
                            ],
                            spacing=4,
                        ),
                        padding=ft.padding.symmetric(horizontal=12, vertical=8),
                        bgcolor="#1A1A1A",
                        border_radius=ft.border_radius.all(8),
                        width=350,
                        on_click=lambda e: print("Selected: Thursday, March 14"),
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    "Friday, March 15",
                                    size=14,
                                    font_family="Instruments Sans",
                                    weight=ft.FontWeight.BOLD,
                                    color="#FFFFFF",
                                ),
                                ft.Text(
                                    "10:00 AM",
                                    size=12,
                                    font_family="Instruments Sans",
                                    color="#FFFFFF",
                                ),
                            ],
                            spacing=4,
                        ),
                        padding=ft.padding.symmetric(horizontal=12, vertical=8),
                        bgcolor="#3A3A3A",
                        border_radius=ft.border_radius.all(8),
                        width=350,
                        on_click=lambda e: print("Selected: Friday, March 15"),
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    "Saturday, March 16",
                                    size=14,
                                    font_family="Instruments Sans",
                                    weight=ft.FontWeight.BOLD,
                                    color="#FFFFFF",
                                ),
                                ft.Text(
                                    "10:00 AM",
                                    size=12,
                                    font_family="Instruments Sans",
                                    color="#FFFFFF",
                                ),
                            ],
                            spacing=4,
                        ),
                        padding=ft.padding.symmetric(horizontal=12, vertical=8),
                        bgcolor="#1A1A1A",
                        border_radius=ft.border_radius.all(8),
                        width=350,
                        on_click=lambda e: print("Selected: Saturday, March 16"),
                    ),
                ],
                spacing=8,
            ),
            padding=ft.padding.only(top=8),
            visible=False,
        )

        date_dropdown = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text(
                        "Select a date",
                        size=14,
                        color="#FFFFFF",
                        font_family="Instruments Sans",
                    ),
                    ft.Icon(
                        name=ft.icons.ARROW_DROP_DOWN,
                        color="#FFFFFF",
                        size=16,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center_left,
            width=350,
            padding=ft.padding.symmetric(horizontal=12, vertical=8),
            bgcolor=ft.colors.with_opacity(0.1, ft.colors.BLACK),
            border=ft.border.all(color="#FFFFFF", width=1),
            border_radius=ft.border_radius.all(8),
            on_click=toggle_dropdown,
        )

        # Sections
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

        # BEFORE YOU BOOK SECTION
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

        # WHAT TO EXPECT SECTION
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

        # Book Now Button
        book_now_button = ft.Container(
            content=ft.ElevatedButton(
                text="Book Now",
                on_click=self.book_now,
                bgcolor="#A2A8BF",
                width=200,
                height=45,
                style=ft.ButtonStyle(
                    text_style=ft.TextStyle(
                        font_family="Intruments Sans",
                        size=16,
                    ),
                    color="#FFFFFF",
                ),
            ),
            alignment=ft.alignment.center,
            padding=ft.padding.only(top=16, bottom=32),
        )

        # Main Content
        main_content = ft.Container(
            content=ft.Column(
                controls=[
                    header,
                    date_dropdown,
                    dropdown_items,
                    before_you_book,
                    what_to_expect,
                    event_details,
                    book_now_button,
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            padding=ft.padding.all(16),
        )

        # Return the full view
        return ft.View(
            route="/dining",
            controls=[ft.Stack(controls=[background, main_content], expand=True)],
        )
