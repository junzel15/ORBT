import flet as ft
from datetime import datetime
import json
from global_state import get_logged_in_user, update_user_data
import uuid


class DiningPage:

    def __init__(self, page: ft.Page, go_to, **kwargs):
        self.page = page
        self.go_to = go_to
        self.page.title = "Dining"
        self.page.theme_mode = None
        self.page.padding = 0
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.text_size = 12
        self.current_tab = None
        self.tab_buttons = {}
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
        self.page.views.clear()
        self.page.go("/homepage")
        self.page.update()

    def render(self):
        self.page.on_resize = self.on_resize

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
        try:
            with open("json/date.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def select_date(self, e, date_str):
        try:
            formatted_date = date_str.upper()
            matching_bookings = [
                b for b in self.bookings if b["select_a_date"] == formatted_date
            ]

            if matching_bookings:
                self.selected_date = formatted_date
                self.selected_time = matching_bookings[0]["select_a_time"]

                self.date_text.value = f"{self.selected_date} - {self.selected_time}"

                if self.date_dropdown:
                    self.date_dropdown.content = ft.Row(
                        controls=[
                            ft.Text(self.selected_date, size=14, color="white"),
                            ft.Text(self.selected_time, size=14, color="white"),
                            ft.Icon(
                                name=ft.icons.ARROW_DROP_DOWN, color="white", size=16
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    )
                    self.date_dropdown.update()

                if self.dropdown_items:
                    self.dropdown_items.visible = False
                    self.dropdown_items.update()

                if self.date_text.page:
                    self.date_text.update()

                self.page.update()

                self.save_date_time_to_user()

            else:
                print(f"No bookings found for {formatted_date}")

        except ValueError as ex:
            print(f"Error parsing date: {date_str} - {ex}")

    def save_date_time_to_user(self):
        user = get_logged_in_user()
        if not user:
            print("No user is logged in.")
            return

        user["selected_date"] = self.selected_date
        user["selected_time"] = self.selected_time

        print(
            f"Date and time saved for user {user['uuid']}: {self.selected_date} - {self.selected_time}"
        )

    def save_event_name(self, event_name):
        user = get_logged_in_user()
        if not user:
            print("No user is logged in.")
            return
        user["event_name"] = event_name
        print(f"Event '{event_name}' saved successfully for user {user['uuid']}.")

    def book_now(self, e):
        user = get_logged_in_user()
        if not user:
            print("No user is logged in.")
            return
        if not self.selected_date or not self.selected_time or not self.current_tab:
            print("Please select a date, time, and tab before booking.")
            return
        print(f"User data before booking: {user}")

        if not user.get("event_name"):
            print("Error: No event selected.")
            return

        self.selected_event_name = user["event_name"]
        print(f"Event Name: {self.selected_event_name}")
        print(f"Selected Tab: {self.current_tab}")

        file_path = "json/booking.json"
        bookings = []
        try:
            with open(file_path, "r") as file:
                bookings = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("No existing bookings or invalid file format. Starting fresh.")

        existing_ids = [
            int(booking["booking_id"].split(" - ")[1])
            for booking in bookings
            if booking.get("booking_id", "").startswith("ORBT -")
        ]
        print(f"Existing Booking IDs: {existing_ids}")

        next_id = None
        for i in range(1, 6):
            if i not in existing_ids:
                next_id = i
                break

        if next_id is None:
            print("Maximum number of bookings reached. Cannot create a new booking.")
            return

        booking_id = f"ORBT - {next_id:03}"
        print(f"Generated Booking ID: {booking_id}")

        new_booking = {
            "uuid": user["uuid"],
            "booking_id": booking_id,
            "date": self.selected_date,
            "time": self.selected_time,
            "location": "Pagadian City",
            "event_name": self.selected_event_name,
            "book_option_order": self.current_tab,
            "status": "Upcoming",
            "venue_name": "Water Front Hotel",
            "Coffee_image": "/assets/images/Coffee.png",
            "Brunch_image": "/assets/images/Brunch.png",
            "Diner_image": "/assets/images/Diner.png",
            "Dining_image": "/assets/images/Icon Dinning.png",
            "Bars_image": "/assets/images/Bars.png",
            "Experiences_image": "/assets/images/Experiences.png",
        }
        print(f"New Booking Before Append: {new_booking}")

        try:
            bookings.append(new_booking)
            print(f"After appending: {len(bookings)} bookings")
            print(f"Updated Data: {bookings}")

            with open(file_path, "w") as file:
                json.dump(bookings, file, indent=4)
                file.flush()
            print("Booking data successfully written to file!")
            with open(file_path, "r") as file:
                print("Final Booking Data:", file.read())

            print(f"Booking successful: {new_booking}")
            self.page.go("/loadingscreen")
            self.page.update()

        except Exception as e:
            print(f"Error: {e}")

    def toggle_dropdown(self, e):
        self.dropdown_items.visible = not self.dropdown_items.visible
        self.dropdown_items.update()
        self.page.update()

    def create_tab_button(self, label):
        return ft.Container(
            content=ft.Text(
                label,
                size=14,
                weight=ft.FontWeight.BOLD,
                color="black" if self.current_tab == label else "white",
            ),
            padding=ft.padding.symmetric(horizontal=20, vertical=10),
            border=ft.border.all(1, "white"),
            border_radius=20,
            alignment=ft.alignment.center,
            bgcolor="white" if self.current_tab == label else "transparent",
            on_click=lambda e: self.select_tab(label),
        )

    def get_button_style(self, label):
        return ft.ButtonStyle(
            color="white" if self.current_tab == label else "white",
            bgcolor="transparent",
            padding=ft.padding.all(10),
        )

    def select_tab(self, tab_name):
        self.current_tab = tab_name
        print(f"Selected tab: {tab_name}")
        user = get_logged_in_user()
        if user:
            user["book_option_order"] = tab_name
            try:
                with open("json/booking.json", "r+") as file:
                    users = json.load(file)
                    for u in users:
                        if u["uuid"] == user["uuid"]:
                            u["book_option_order"] = tab_name
                            break
                    file.seek(0)
                    json.dump(users, file, indent=4)
                    file.truncate()
                update_user_data(user)
                print(f"Tab {tab_name} saved successfully to user data.")
            except (FileNotFoundError, json.JSONDecodeError) as ex:
                print(f"Error saving user data: {ex}")
        else:
            print("No user is logged in.")

        for label, button in self.tab_buttons.items():
            button.bgcolor = "white" if label == self.current_tab else "transparent"
            button.content.color = "black" if label == self.current_tab else "white"
            button.update()

        self.page.update()

    def render(self):
        self.page.on_resize = self.on_resize
        date_list = sorted(
            {b["select_a_date"] for b in self.bookings},
            key=lambda date: datetime.strptime(date, "%B %d, %Y"),
        )

        tab_labels = ["Coffee", "Brunch", "Diner"]

        tab_section = ft.Row(
            controls=[self.create_tab_button(label) for label in tab_labels],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=12,
        )
        self.tab_buttons = {
            label: btn for label, btn in zip(tab_labels, tab_section.controls)
        }

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

        self.dropdown_items = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(date, size=14, color="#FFFFFF"),
                                ft.Text(
                                    next(
                                        (
                                            b["select_a_time"]
                                            for b in self.bookings
                                            if b["select_a_date"] == date
                                        ),
                                        "N/A",
                                    ),
                                    size=14,
                                    color="#A0A0A0",
                                ),
                            ],
                            spacing=2,
                        ),
                        padding=8,
                        bgcolor=ft.colors.with_opacity(0.1, ft.colors.BLACK),
                        border_radius=4,
                        on_click=lambda e, d=date: self.select_date(e, d),
                    )
                    for date in date_list
                ],
                spacing=4,
            ),
            padding=8,
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
                on_click=self.book_now,
                style=ft.ButtonStyle(
                    bgcolor={
                        ft.MaterialState.DEFAULT: "#A2A8BF",
                        ft.MaterialState.HOVERED: ft.colors.BLUE,
                    },
                    color="#FFFFFF",
                    padding=ft.padding.symmetric(horizontal=20, vertical=10),
                    text_style=ft.TextStyle(
                        font_family="Instruments Sans",
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
            route="/diner",
            controls=[
                ft.Stack(
                    controls=[background, main_content],
                    expand=True,
                )
            ],
        )
