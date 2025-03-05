import flet as ft
from global_state import get_logged_in_user
from dynamodb.dynamoDB_bookings import dynamo_read, dynamo_write


class BookingDetails(ft.UserControl):
    def __init__(self, page: ft.Page, go_to, booking_id=None):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.user_data = get_logged_in_user()
        self.booking_id = booking_id

        self.set_mobile_view()

        self.page.on_resize = self.adjust_window_size
        self.adjust_window_size()
        self.page.update()

    def set_mobile_view(self):
        self.page.window_width = 400
        self.page.window_height = 800

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

    def get_booking_details(self):
        try:
            if self.booking_id:
                print(f"Fetching booking for ID: {self.booking_id}")
                booking = dynamo_read("bookings", "booking_id", self.booking_id)
                if isinstance(booking, dict):
                    return booking
                print(f"Booking ID {self.booking_id} not found or invalid format!")

            logged_in_user = get_logged_in_user()
            print(f"Logged-in user: {logged_in_user}")

            if not logged_in_user:
                print("No logged-in user found.")
                return None

            user_uuid = logged_in_user.get("uuid")
            print(f"Fetching booking for user UUID: {user_uuid}")

            if not user_uuid:
                print("User UUID is missing.")
                return None

            user_bookings = dynamo_read("bookings", "uuid", user_uuid)

            if isinstance(user_bookings, dict):
                return user_bookings
            elif isinstance(user_bookings, list) and user_bookings:
                return user_bookings[-1]

            return None
        except Exception as e:
            print(f"Error getting booking details: {e}")
            return None

    def cancel_event(self, e):
        self.booking = self.get_booking_details()

        if self.booking:
            booking_id = self.booking.get("booking_id")
            if not booking_id:
                print("Error: Booking does not have a 'booking_id' key.")
                return

            print(f"Cancelling booking with ID: {booking_id}")

            self.booking["status"] = "Cancelled"

            self.save_cancelled_booking(self.booking)

            print(
                f"Booking ID {booking_id} status updated to: {self.booking['status']}"
            )

            self.go_to("/cancelbooking", self.page)
        else:
            print("Error: No booking selected to cancel.")

    def save_cancelled_booking(self, booking):
        try:
            booking_id = booking.get("booking_id")
            if not booking_id:
                print("Error: Booking does not have a 'booking_id' key.")
                return

            updated_booking = {**booking, "status": "Cancelled"}
            dynamo_write("bookings", updated_booking)

            print(f"Booking {booking_id} marked as Cancelled.")
        except Exception as e:
            print(f"Error updating cancelled booking: {e}")

    def build(self):
        self.booking = self.get_booking_details()

        date_time_str = "Date/Time not available"
        event_name = "Unknown Event"
        book_option_order = "Unknown"
        image_path = "assets/images/default.png"

        if self.booking:
            date_str = self.booking.get("date", "Unknown Date")
            time_str = self.booking.get("time", "Unknown Time")
            date_time_str = f"{date_str}\n{time_str}"
            event_name = self.booking.get("event_name", "Unknown Event")
            book_option_order = self.booking.get("book_option_order", "Unknown")

            if event_name in ["Bars", "Experiences"]:
                image_path = self.booking.get(
                    f"{event_name}_image", "assets/images/default.png"
                ).lstrip("/")
                book_option_order = ""
            else:
                image_path = self.booking.get(
                    f"{book_option_order}_image", "assets/images/default.png"
                ).lstrip("/")

            print(f"✅ Displaying: {event_name} on {date_time_str}")

        booking_id = (
            self.booking.get("booking_id", "No ID") if self.booking else "No ID"
        )

        self.page.assets_dir = "assets"

        return ft.Container(
            image_src="assets/images/Dark Background 2 Screen.png",
            image_fit=ft.ImageFit.COVER,
            padding=20,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.IconButton(
                                icon=ft.icons.ARROW_BACK,
                                icon_color="white",
                                on_click=lambda _: self.go_to("/homepage", self.page),
                            ),
                            ft.Text(
                                booking_id,
                                color="white",
                                weight="bold",
                            ),
                        ],
                        alignment="spaceBetween",
                    ),
                    ft.Row(
                        [
                            ft.Column(
                                [
                                    *(
                                        [
                                            ft.Text(
                                                book_option_order,
                                                color="white",
                                                size=10,
                                            )
                                        ]
                                        if book_option_order
                                        else []
                                    ),
                                    ft.Text(
                                        event_name,
                                        color="white",
                                        font_family="Sora",
                                        size=24,
                                        weight="bold",
                                    ),
                                    ft.Row(
                                        [
                                            ft.Icon(
                                                ft.icons.CALENDAR_MONTH,
                                                color="white",
                                                size=14,
                                            ),
                                            ft.Text(
                                                date_time_str,
                                                color="white",
                                                size=12,
                                            ),
                                        ]
                                    ),
                                    ft.Row(
                                        [
                                            ft.Icon(
                                                ft.icons.LOCATION_ON,
                                                color="white",
                                                size=14,
                                            ),
                                            ft.Text(
                                                "To Be Revealed 🤯",
                                                color="white",
                                                size=12,
                                            ),
                                        ]
                                    ),
                                ]
                            ),
                            ft.Image(src=image_path, width=100, height=100),
                        ],
                        alignment="spaceBetween",
                    ),
                    ft.Divider(color="white", thickness=1),
                    ft.Row(
                        [
                            ft.Icon(ft.icons.FAVORITE_BORDER, color="white"),
                            ft.Text(
                                "Common Interests:",
                                color="white",
                                weight="bold",
                                size=14,
                                font_family="Instrument Sans",
                            ),
                        ],
                        spacing=5,
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                ft.Text(
                                    "Technology",
                                    color="white",
                                    size=10,
                                    font_family="Instrument Sans",
                                ),
                                padding=10,
                                border=ft.border.all(1, "white"),
                                border_radius=20,
                            ),
                            ft.Container(
                                ft.Text(
                                    "Politics",
                                    color="white",
                                    size=10,
                                    font_family="Instrument Sans",
                                ),
                                padding=10,
                                border=ft.border.all(1, "white"),
                                border_radius=20,
                            ),
                            ft.Container(
                                ft.Text(
                                    "Healthcare",
                                    color="white",
                                    size=10,
                                    font_family="Instrument Sans",
                                ),
                                padding=10,
                                border=ft.border.all(1, "white"),
                                border_radius=20,
                            ),
                            ft.Container(
                                ft.Text(
                                    "Academia & Research",
                                    color="white",
                                    size=10,
                                    font_family="Instrument Sans",
                                ),
                                padding=10,
                                border=ft.border.all(1, "white"),
                                border_radius=20,
                            ),
                        ],
                        spacing=10,
                        wrap=True,
                        alignment="start",
                    ),
                    ft.Divider(color="white", thickness=1),
                    ft.Row(
                        [
                            ft.Icon(
                                ft.icons.FLAG_CIRCLE,
                                color="white",
                                size=16,
                            ),
                            ft.Text(
                                "Nationality",
                                color="white",
                                weight="bold",
                                width=200,
                                size=14,
                            ),
                            ft.Text(
                                "Language:",
                                color="white",
                                weight="bold",
                                font_family="Instrument Sans",
                                size=14,
                            ),
                        ]
                    ),
                    ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.Image(
                                                src="images/US.png",
                                                width=20,
                                                height=20,
                                            ),
                                            ft.Text(
                                                "United States of America",
                                                color="white",
                                                font_family="Instrument Sans",
                                                size=12,
                                            ),
                                        ]
                                    ),
                                    ft.Row(
                                        [
                                            ft.Image(
                                                src="images/PH.png",
                                                width=20,
                                                height=20,
                                            ),
                                            ft.Text(
                                                "Philippines",
                                                color="white",
                                                font_family="Instrument Sans",
                                                size=12,
                                            ),
                                        ]
                                    ),
                                ]
                            ),
                            ft.Row(
                                [
                                    ft.Text(
                                        "English, Filipino",
                                        color="white",
                                        font_family="Instrument Sans",
                                        size=12,
                                    ),
                                ],
                                alignment="start",
                            ),
                        ],
                        alignment="spaceBetween",
                    ),
                    ft.Divider(color="white", thickness=1),
                    ft.Row(
                        [
                            ft.Icon(
                                ft.icons.STAR,
                                color="white",
                                size=16,
                            ),
                            ft.Text(
                                "Zodiac Signs:",
                                color="white",
                                weight="bold",
                                font_family="Instrument Sans",
                                size=14,
                            ),
                        ]
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.Image(
                                            src="images/Icon Aries.png",
                                            width=25,
                                            height=25,
                                        ),
                                        ft.Text(
                                            "Aries",
                                            color="white",
                                            font_family="Instrument Sans",
                                            size=12,
                                        ),
                                    ]
                                )
                            ),
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.Image(
                                            src="images/Icon Taurus.png",
                                            width=25,
                                            height=25,
                                        ),
                                        ft.Text(
                                            "Taurus",
                                            color="white",
                                            font_family="Instrument Sans",
                                            size=12,
                                        ),
                                    ]
                                )
                            ),
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.Image(
                                            src="images/Icon Gemini.png",
                                            width=25,
                                            height=25,
                                        ),
                                        ft.Text(
                                            "Gemini",
                                            color="white",
                                            font_family="Instrument Sans",
                                            size=12,
                                        ),
                                    ]
                                )
                            ),
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.Image(
                                            src="images/Icon Cancer.png",
                                            width=25,
                                            height=25,
                                        ),
                                        ft.Text(
                                            "Cancer",
                                            color="white",
                                            font_family="Instrument Sans",
                                            size=12,
                                        ),
                                    ]
                                )
                            ),
                        ],
                        spacing=10,
                        alignment="start",
                    ),
                    ft.Divider(color="white", thickness=1),
                    ft.Text(
                        "E-Ticket will be revealed 1 day before the event. Stay tuned!",
                        color="white",
                        size=14,
                        text_align="center",
                        font_family="Instrument Sans",
                    ),
                    ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Container(
                                        ft.Text(
                                            "4",
                                            color="white",
                                            size=16,
                                            weight="bold",
                                            font_family="Instrument Sans",
                                        ),
                                        padding=6,
                                        border=ft.border.all(1, "white"),
                                        border_radius=6,
                                        width=35,
                                        alignment=ft.alignment.center,
                                    ),
                                    ft.Text(
                                        "DAYS",
                                        color="white",
                                        size=10,
                                        text_align="center",
                                        font_family="Instrument Sans",
                                    ),
                                ],
                                alignment="center",
                            ),
                            ft.Container(
                                ft.Text(
                                    ":",
                                    color="white",
                                    size=14,
                                    weight="bold",
                                    font_family="Instrument Sans",
                                ),
                                alignment=ft.alignment.center,
                                padding=6,
                            ),
                            ft.Column(
                                [
                                    ft.Container(
                                        ft.Text(
                                            "10",
                                            color="white",
                                            size=16,
                                            weight="bold",
                                            font_family="Instrument Sans",
                                        ),
                                        padding=6,
                                        border=ft.border.all(1, "white"),
                                        border_radius=6,
                                        width=35,
                                        alignment=ft.alignment.center,
                                    ),
                                    ft.Text(
                                        "HOURS",
                                        color="white",
                                        size=10,
                                        text_align="center",
                                        font_family="Instrument Sans",
                                    ),
                                ],
                                alignment="center",
                            ),
                            ft.Container(
                                ft.Text(
                                    ":",
                                    color="white",
                                    size=14,
                                    weight="bold",
                                    font_family="Instrument Sans",
                                ),
                                alignment=ft.alignment.center,
                                padding=6,
                            ),
                            ft.Column(
                                [
                                    ft.Container(
                                        ft.Text(
                                            "12",
                                            color="white",
                                            size=16,
                                            weight="bold",
                                            font_family="Instrument Sans",
                                        ),
                                        padding=6,
                                        border=ft.border.all(1, "white"),
                                        border_radius=6,
                                        width=35,
                                        alignment=ft.alignment.center,
                                    ),
                                    ft.Text(
                                        "MIN",
                                        color="white",
                                        size=10,
                                        text_align="center",
                                        font_family="Instrument Sans",
                                    ),
                                ],
                                alignment="center",
                            ),
                        ],
                        alignment="center",
                        spacing=5,
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                "Cancel Event",
                                bgcolor="white",
                                color="black",
                                width=150,
                                on_click=self.cancel_event,
                            ),
                            ft.ElevatedButton(
                                "View E-Ticket",
                                bgcolor="#3A1A6A",
                                color="white",
                                width=150,
                            ),
                        ],
                        alignment="center",
                        spacing=10,
                    ),
                ]
            ),
        )
