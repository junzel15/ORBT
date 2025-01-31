import flet as ft


class DiningDinerPage:
    def __init__(self, page: ft.Page, go_to):

        self.page = page
        self.go_to = go_to
        self.page.title = "Dining"
        self.page.theme_mode = None
        self.page.padding = 0
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.text_size = 12
        self.current_tab = "diner"
        self.expanded_state = {"before": False, "expect": False}

        self.before_toggle_ref = ft.Ref[ft.Text]()
        self.expect_toggle_ref = ft.Ref[ft.Text]()
        self.before_content_ref = ft.Ref[ft.Container]()
        self.expect_content_ref = ft.Ref[ft.Container]()

    def on_resize(self, e):
        pass

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

    def book_now(self, e):
        self.go_to("/")

    def render(self):
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
                    on_click=lambda e: (
                        self.page.views.pop(),
                        self.page.go("/homepage"),
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        def toggle_dropdown(e):
            dropdown_items.visible = not dropdown_items.visible
            dropdown_items.update()

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

        main_content = ft.Container(
            content=ft.Column(
                controls=[
                    header,
                    tab_section,
                    date_dropdown,
                    dropdown_items,
                    before_you_book,
                    what_to_expect,
                    event_details,
                    book_now_button,
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll="always",
            ),
            expand=True,
            padding=ft.padding.all(16),
        )

        return ft.View(
            route="/diner",
            controls=[ft.Stack(controls=[background, main_content], expand=True)],
        )
