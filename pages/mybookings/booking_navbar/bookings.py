import flet as ft
import os
from global_state import get_logged_in_user
from pages.mybookings.booking_navbar.components import BookingCard, Tabs, FilterModal
from pages.mybookings.booking_navbar.helpers import filter_bookings
from dynamodb.dynamoDB_bookings import dynamo_read_all, dynamo_write


class Bookings(ft.UserControl):
    def __init__(self, page=None, go_to=None):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.current_tab = "Upcoming"

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

        self.original_bookings = self.load_bookings()
        self.filtered_bookings = self.original_bookings

        self.bookings_list = ft.ListView(
            expand=True,
            spacing=15,
            padding=ft.padding.symmetric(horizontal=15),
            auto_scroll=False,
        )

        self.filter_modal = FilterModal(self.apply_filter)
        self.tabs = Tabs(self.switch_tab)

        self.tab_indicator = ft.Container(
            height=4,
            width=60,
            bgcolor="white",
            animate=ft.animation.Animation(300, "ease_out"),
        )

        self.tabs_row = self.build_tabs_row()

        self.bottom_nav = ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        content=ft.Image(src="images/Home.png", width=28, height=28),
                        on_click=lambda _: self.go_to("/homepage", self.page),
                    ),
                    ft.IconButton(
                        content=ft.Image(src="images/Star.png", width=28, height=28),
                        on_click=lambda _: self.go_to("/bookings", self.page),
                    ),
                    ft.IconButton(
                        content=ft.Image(src="images/Message.png", width=28, height=28),
                        on_click=lambda _: self.go_to("/messages", self.page),
                    ),
                    ft.IconButton(
                        content=ft.Image(src="images/Profile.png", width=28, height=28),
                        on_click=lambda _: self.go_to("/profile", self.page),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            bgcolor="white",
            border_radius=30,
            padding=ft.padding.symmetric(vertical=10),
            shadow=ft.BoxShadow(blur_radius=5, color="#00000020"),
        )

    def did_mount(self):
        self.update_bookings_view()

    def build(self):
        logged_in_user = get_logged_in_user()
        print(f"Logged in user: {logged_in_user}")

        self.tabs_row = ft.Container(
            content=ft.Stack(
                [
                    ft.Row(
                        controls=[
                            ft.GestureDetector(
                                on_tap=lambda _: self.switch_tab("Upcoming"),
                                content=ft.Container(
                                    content=ft.Text(
                                        "Upcoming",
                                        size=14,
                                        weight="bold",
                                        color=(
                                            "blue"
                                            if self.current_tab == "Upcoming"
                                            else "white"
                                        ),
                                    ),
                                    bgcolor=(
                                        "white"
                                        if self.current_tab == "Upcoming"
                                        else "black"
                                    ),
                                    padding=ft.padding.symmetric(
                                        horizontal=15, vertical=8
                                    ),
                                    border_radius=ft.border_radius.only(
                                        top_left=15, bottom_left=15
                                    ),
                                ),
                            ),
                            ft.GestureDetector(
                                on_tap=lambda _: self.switch_tab("Completed"),
                                content=ft.Container(
                                    content=ft.Text(
                                        "Completed",
                                        size=14,
                                        weight="bold",
                                        color=(
                                            "blue"
                                            if self.current_tab == "Completed"
                                            else "white"
                                        ),
                                    ),
                                    bgcolor=(
                                        "white"
                                        if self.current_tab == "Completed"
                                        else "black"
                                    ),
                                    padding=ft.padding.symmetric(
                                        horizontal=15, vertical=8
                                    ),
                                ),
                            ),
                            ft.GestureDetector(
                                on_tap=lambda _: self.switch_tab("Cancelled"),
                                content=ft.Container(
                                    content=ft.Text(
                                        "Cancelled",
                                        size=14,
                                        weight="bold",
                                        color=(
                                            "blue"
                                            if self.current_tab == "Cancelled"
                                            else "white"
                                        ),
                                    ),
                                    bgcolor=(
                                        "white"
                                        if self.current_tab == "Cancelled"
                                        else "black"
                                    ),
                                    padding=ft.padding.symmetric(
                                        horizontal=15, vertical=8
                                    ),
                                    border_radius=ft.border_radius.only(
                                        top_right=15, bottom_right=15
                                    ),
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    self.tab_indicator,
                ]
            ),
            padding=ft.padding.only(top=5),
        )

        return ft.Container(
            expand=True,
            height=self.page.height,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(
                        width=self.page.width,
                        image_src="assets/images/Rectangle.png",
                        image_fit=ft.ImageFit.COVER,
                        content=ft.Column(
                            spacing=10,
                            controls=[
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.ARROW_BACK,
                                            icon_color="white",
                                            on_click=lambda _: self.go_to(
                                                "/homepage", self.page
                                            ),
                                        ),
                                        ft.Text(
                                            "My Bookings",
                                            size=20,
                                            weight="bold",
                                            color="white",
                                        ),
                                        ft.IconButton(
                                            icon=ft.icons.TUNE,
                                            icon_color="white",
                                            on_click=lambda _: self.filter_modal.open(),
                                        ),
                                    ],
                                ),
                                ft.Container(
                                    content=ft.TextField(
                                        hint_text="Search Events, Dates, Places ...",
                                        prefix_icon=ft.icons.SEARCH,
                                        border_radius=25,
                                        border_color="white",
                                        color="black",
                                        bgcolor="white",
                                        height=40,
                                        width=self.page.width * 0.9,
                                    ),
                                    padding=ft.padding.symmetric(horizontal=15),
                                ),
                                self.tabs_row,
                            ],
                        ),
                        padding=ft.padding.only(top=30, left=10, right=10),
                    ),
                    ft.Container(
                        expand=True,
                        content=self.bookings_list,
                        padding=ft.padding.symmetric(horizontal=15),
                    ),
                    ft.Container(
                        height=60,
                        content=self.bottom_nav,
                    ),
                ],
            ),
        )

    def switch_tab(self, tab_name):
        print(f"Tab selected: {tab_name}")
        self.current_tab = tab_name

        tab_positions = {
            "Upcoming": 0,
            "Completed": self.page.width / 3,
            "Cancelled": (self.page.width / 3) * 2,
        }
        self.tab_indicator.left = tab_positions[tab_name]
        self.tabs_row.content = self.build_tabs_row()
        self.update_bookings_view()
        self.update()

    def build_tabs_row(self):
        return ft.Stack(
            [
                ft.Row(
                    controls=[
                        self.build_tab("Upcoming"),
                        self.build_tab("Completed"),
                        self.build_tab("Cancelled"),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                self.tab_indicator,
            ]
        )

    def build_tab(self, tab_name):
        is_active = self.current_tab == tab_name
        return ft.GestureDetector(
            on_tap=lambda _: self.switch_tab(tab_name),
            content=ft.Container(
                content=ft.Text(
                    tab_name,
                    size=14,
                    weight="bold",
                    color="blue" if is_active else "white",
                ),
                bgcolor="white" if is_active else "black",
                padding=ft.padding.symmetric(horizontal=20, vertical=10),
                border_radius=ft.border_radius.only(
                    top_left=15 if tab_name == "Upcoming" else 0,
                    bottom_left=15 if tab_name == "Upcoming" else 0,
                    top_right=15 if tab_name == "Cancelled" else 0,
                    bottom_right=15 if tab_name == "Cancelled" else 0,
                ),
            ),
        )

    def apply_filter(self, filters):
        print(f"Applying filters: {filters}")
        self.filtered_bookings = filter_bookings(self.original_bookings, filters)
        self.update_bookings_view()

    def update_bookings_view(self):
        print("Updating bookings view... Total bookings:", len(self.filtered_bookings))

        self.bookings_list.controls.clear()

        filtered = [
            b
            for b in self.filtered_bookings
            if b.get("status", "").strip().lower() == self.current_tab.lower()
        ]

        if not filtered:
            print(f"No bookings found for {self.current_tab}")
            self.bookings_list.controls.append(
                ft.Text(
                    f"No bookings available for {self.current_tab}.",
                    size=16,
                    color="gray",
                )
            )
        else:
            for booking in filtered:
                print(
                    f"Adding booking: {booking['event_name']} on {booking.get('date', 'Unknown')}"
                )
                booking_card = BookingCard(
                    booking, self.page, self.update_lists, self.go_to
                )
                self.bookings_list.controls.append(booking_card.build())

        self.bookings_list.update()
        self.update()

    def update_lists(self, updated_booking):
        print(f"Updating lists with booking: {updated_booking}")

        for booking in self.original_bookings:
            if booking["booking_id"] == updated_booking["booking_id"]:
                booking["status"] = updated_booking["status"]
                break

        if updated_booking["status"] == "Cancelled":
            dynamo_write("bookings", updated_booking)
            self.save_cancelled_booking(updated_booking)

        self.update_bookings_view()

    def save_cancelled_booking(self, booking):
        try:
            booking_id = booking.get("booking_id")
            user_uuid = booking.get("uuid")

            if not booking_id or not user_uuid:
                print("Error: Booking does not have a 'booking_id' or 'uuid' key.")
                return

            updated_booking = booking.copy()
            updated_booking["status"] = "Cancelled"

            success = dynamo_write("bookings", updated_booking)
            if not success:
                print(f"Error: Failed to update booking {booking_id} in the database.")
                return

            print(f"Booking {booking_id} successfully marked as Cancelled.")

            self.original_bookings = self.load_bookings()
            self.filtered_bookings = self.original_bookings
            self.update_bookings_view()

        except Exception as e:
            print(f"Error saving cancelled booking: {e}")

    def load_user_bookings(self):
        user = get_logged_in_user()
        if not user:
            print("No user is logged in.")
            return []

        user_uuid = user["uuid"]
        try:
            items = dynamo_read_all("bookings")
            user_bookings = [item for item in items if item.get("uuid") == user_uuid]
            return user_bookings
        except Exception as e:
            print(f"Error loading user bookings: {e}")
            return []

    def load_bookings(self):
        logged_in_user = get_logged_in_user()
        if not logged_in_user:
            print("No logged-in user found.")
            return []

        try:
            user_bookings = dynamo_read_all("bookings")
            if not user_bookings:
                return []

            user_bookings_list = []

            for booking in user_bookings:
                event_name = booking.get("event_name", "Unknown")
                book_option_order = booking.get("book_option_order", "Unknown")
                venue_name = booking.get("venue_name", "Unknown")
                booking_uuid = booking.get("uuid")
                booking_id = booking.get("booking_id", "No ID")
                formatted_date = booking.get("date", "Unknown Date").strip()
                time_str = booking.get("time", "Unknown Time")

                image_key = f"{event_name}_image"
                image_path = booking.get(image_key, "assets/images/default.png")

                image_path = os.path.join(
                    "assets", "images", os.path.basename(image_path)
                )

                if not os.path.exists(image_path):
                    print(f"Image not found: {image_path}, using default.")
                    image_path = "assets/images/default.png"

                user_bookings_list.append(
                    {
                        "uuid": booking_uuid,
                        "booking_id": booking_id,
                        "event_name": event_name,
                        "emoji": "🍽️",
                        "status": booking.get("status", "Upcoming"),
                        "time": time_str,
                        "date": formatted_date,
                        "location": booking.get("location", "Unknown Location"),
                        "venue_name": venue_name,
                        "category": book_option_order.upper(),
                        "image": image_path,
                        "book_option_order": book_option_order,
                    }
                )

            print(f"Loaded {len(user_bookings_list)} bookings with images.")
            return user_bookings_list

        except Exception as e:
            print(f"Error loading bookings: {e}")
            return []

    @staticmethod
    def get_booking_image(booking):
        event_name = booking.get("event_name", "Unknown")
        book_option_order = booking.get("book_option_order", "Unknown")

        if event_name in ["Bars", "Experiences"]:
            return booking.get(
                f"{event_name}_image", "assets/images/default.png"
            ).lstrip("/")
        return booking.get(
            f"{book_option_order}_image", "assets/images/default.png"
        ).lstrip("/")
