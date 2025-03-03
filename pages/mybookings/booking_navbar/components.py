import flet as ft
import os


class BookingCard(ft.UserControl):

    def __init__(self, booking, page, update_lists=None, go_to=None):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.booking = booking
        self.update_lists = update_lists

    def cancel_booking(self, e=None):
        self.booking["status"] = "Cancelled"
        if self.update_lists:
            self.update_lists(self.booking)
        self.update()

    def build(self):
        status = self.booking["status"]

        if status == "Upcoming":
            return self.upcoming_card()
        elif status == "Completed":
            return self.completed_card()
        elif status == "Cancelled":
            return self.cancelled_card()

    def upcoming_card(self):
        event_name = self.booking.get("event_name", "Unknown Event")
        image_path = self.booking.get("image", "assets/images/default.png")
        image_path = os.path.join("assets", "images", os.path.basename(image_path))

        if not os.path.exists(image_path):
            print(f"Image not found: {image_path}, using default.")
            image_path = "assets/images/default.png"

        show_category = event_name not in ["Bars", "Experiences"]

        return ft.Column(
            spacing=10,
            controls=[
                ft.Container(
                    content=ft.Column(
                        spacing=10,
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Row(
                                        spacing=5,
                                        controls=[
                                            ft.Image(
                                                src=image_path,
                                                width=24,
                                                height=24,
                                                fit=ft.ImageFit.CONTAIN,
                                            ),
                                            ft.Text(event_name, size=16, weight="bold"),
                                            ft.Icon(
                                                name=ft.icons.STAR,
                                                color="orange",
                                                size=14,
                                            ),
                                        ],
                                    ),
                                    ft.Container(
                                        content=ft.Text(
                                            self.booking.get("category", "").upper(),
                                            size=10,
                                            weight="bold",
                                        ),
                                        bgcolor="white",
                                        border=ft.border.all(1, "black"),
                                        border_radius=10,
                                        padding=ft.padding.symmetric(
                                            horizontal=10, vertical=3
                                        ),
                                        visible=show_category,
                                    ),
                                ],
                            ),
                            ft.Divider(height=1, color="black"),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Column(
                                        spacing=2,
                                        controls=[
                                            ft.Text(
                                                "DATE & TIME",
                                                size=10,
                                                color="gray",
                                                weight="bold",
                                            ),
                                            ft.Text(
                                                self.booking.get("date", "Unknown"),
                                                size=14,
                                                weight="bold",
                                            ),
                                            ft.Text(
                                                self.booking.get("time", "Unknown"),
                                                size=14,
                                                weight="bold",
                                            ),
                                        ],
                                    ),
                                    ft.Column(
                                        spacing=2,
                                        controls=[
                                            ft.Text(
                                                "LOCATION",
                                                size=10,
                                                color="gray",
                                                weight="bold",
                                            ),
                                            ft.Text(
                                                self.booking.get(
                                                    "venue_name", "Unknown Venue"
                                                ),
                                                size=14,
                                                weight="bold",
                                                color="black",
                                            ),
                                            ft.Text(
                                                spans=[
                                                    ft.TextSpan(
                                                        text=self.booking.get(
                                                            "location",
                                                            "Location Not Found",
                                                        ),
                                                        style=ft.TextStyle(
                                                            size=14,
                                                            color="black",
                                                            weight="bold",
                                                            decoration=ft.TextDecoration.UNDERLINE,
                                                        ),
                                                    )
                                                ]
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.ElevatedButton(
                                        text="Cancel",
                                        on_click=self.cancel_booking,
                                        style=ft.ButtonStyle(
                                            bgcolor={
                                                ft.MaterialState.DEFAULT: "transparent",
                                                ft.MaterialState.HOVERED: "red",
                                            },
                                            color="black",
                                            padding=ft.padding.symmetric(
                                                horizontal=20, vertical=8
                                            ),
                                            text_style=ft.TextStyle(
                                                size=14, weight="bold"
                                            ),
                                        ),
                                    ),
                                    ft.ElevatedButton(
                                        text="View Details",
                                        on_click=lambda _: (
                                            self.go_to(
                                                "/bookingdetails",
                                                self.page,
                                                booking_id=self.booking["id"],
                                            )
                                            if self.go_to
                                            else print(
                                                "Error: go_to function is not set"
                                            )
                                        ),
                                        style=ft.ButtonStyle(
                                            bgcolor={ft.MaterialState.DEFAULT: "blue"},
                                            color="white",
                                            padding=ft.padding.symmetric(
                                                horizontal=20, vertical=8
                                            ),
                                            text_style=ft.TextStyle(
                                                size=14, weight="bold"
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    padding=15,
                    border_radius=15,
                    bgcolor="#EFE6FF",
                ),
            ],
        )

    def completed_card(self):
        return ft.Container(
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Row(
                                spacing=5,
                                controls=[
                                    ft.Icon(ft.icons.LOCATION_ON, size=16),
                                    ft.Text(
                                        self.booking["title"], size=16, weight="bold"
                                    ),
                                ],
                            ),
                            ft.Container(
                                content=ft.Text(
                                    self.booking["category"].upper(),
                                    size=10,
                                    weight="bold",
                                ),
                                bgcolor="white",
                                border=ft.border.all(1, "black"),
                                border_radius=10,
                                padding=ft.padding.symmetric(horizontal=10, vertical=3),
                            ),
                        ],
                    ),
                    ft.Divider(height=1, thickness=1, color="black"),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Column(
                                spacing=2,
                                controls=[
                                    ft.Text(
                                        self.booking["day"]
                                        + ", "
                                        + self.booking["time"],
                                        size=12,
                                        weight="bold",
                                    ),
                                    ft.Text(self.booking["location"], size=12),
                                ],
                            ),
                        ],
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(
                                "Booking Completed!",
                                size=12,
                                color="#6236FF",
                                weight="bold",
                            ),
                            ft.Text(
                                str(self.booking.get("id", "N/A")),
                                size=12,
                                weight="bold",
                            ),
                        ],
                    ),
                ],
            ),
            padding=15,
            border_radius=15,
            bgcolor="white",
            border=ft.border.all(1, "black"),
        )

    def cancelled_card(self):
        event_name = self.booking["event_name"]
        image_path = self.booking.get("image", "assets/images/default.png")
        image_path = os.path.join("assets", "images", os.path.basename(image_path))

        if not os.path.exists(image_path):
            print(f"Image not found: {image_path}, using default.")
            image_path = "assets/images/default.png"

        show_category = event_name not in ["Bars", "Experiences"]

        return ft.Column(
            spacing=10,
            controls=[
                ft.Container(
                    content=ft.Column(
                        spacing=10,
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Row(
                                        spacing=5,
                                        controls=[
                                            ft.Icon(
                                                name=ft.icons.LOCATION_ON_OUTLINED,
                                                size=24,
                                                color="#6D6D6D",
                                            ),
                                            ft.Text(
                                                self.booking.get(
                                                    "venue_name", "Unknown"
                                                ),
                                                size=16,
                                                weight="bold",
                                                color="#6D6D6D",
                                            ),
                                        ],
                                    ),
                                    ft.Container(
                                        content=ft.Text(
                                            self.booking["category"].upper(),
                                            size=10,
                                            weight="bold",
                                            color="#6D6D6D",
                                        ),
                                        bgcolor="white",
                                        border=ft.border.all(1, "#6D6D6D"),
                                        border_radius=10,
                                        padding=ft.padding.symmetric(
                                            horizontal=10, vertical=3
                                        ),
                                        visible=show_category,
                                    ),
                                ],
                            ),
                            ft.Divider(height=1, color="#6D6D6D"),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Column(
                                        spacing=3,
                                        controls=[
                                            ft.Text(
                                                self.booking.get("date", "Unknown"),
                                                size=12,
                                                weight="bold",
                                                color="#6D6D6D",
                                            ),
                                            ft.Text(
                                                self.booking["time"],
                                                size=12,
                                                weight="bold",
                                                color="#6D6D6D",
                                            ),
                                            ft.Text(
                                                self.booking["location"],
                                                size=12,
                                                color="#6D6D6D",
                                            ),
                                        ],
                                    ),
                                    ft.Text(
                                        str(self.booking.get("event_name", "N/A")),
                                        size=12,
                                        weight="bold",
                                        color="#6D6D6D",
                                    ),
                                ],
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Text(
                                        "Cancelled", size=14, color="red", weight="bold"
                                    ),
                                    ft.Text(
                                        str(self.booking.get("id", "N/A")),
                                        size=12,
                                        weight="bold",
                                        color="#6D6D6D",
                                    ),
                                ],
                            ),
                        ],
                    ),
                    padding=15,
                    border_radius=15,
                    bgcolor="white",
                    border=ft.border.all(1, "#6D6D6D"),
                ),
            ],
        )


class Tabs(ft.UserControl):
    def __init__(self, on_tab_change):
        super().__init__()
        self.on_tab_change = on_tab_change

    def handle_tab_change(self, e):
        if e.control and e.control.selected_index is not None:
            selected_tab_text = e.control.tabs[e.control.selected_index].text
            self.on_tab_change(selected_tab_text)

    def build(self):
        return ft.Tabs(
            selected_index=0,
            on_change=self.handle_tab_change,
            tabs=[
                ft.Tab(text="Upcoming"),
                ft.Tab(text="Completed"),
                ft.Tab(text="Cancelled"),
            ],
            indicator_color="purple",
        )


class FilterModal(ft.UserControl):
    def __init__(self, apply_filter):
        super().__init__()
        self.apply_filter = apply_filter
        self.dialog = None

    def open(self):
        self.dialog.open = True
        self.update()

    def build(self):
        self.dialog = ft.AlertDialog(
            open=False,
            title=ft.Text("Filter"),
            content=ft.Column(
                [
                    ft.TextField(label="Location"),
                    ft.Slider(min=0, max=100, label="Distance"),
                    ft.Row(
                        [
                            ft.Checkbox(label="Dining"),
                            ft.Checkbox(label="Bars"),
                            ft.Checkbox(label="Experiences"),
                        ]
                    ),
                    ft.Row([ft.Checkbox(label="Free"), ft.Checkbox(label="Paid")]),
                ]
            ),
            actions=[
                ft.TextButton("Reset"),
                ft.TextButton(
                    "Apply",
                    on_click=lambda _: self.apply_filter({"example_filter": True}),
                ),
            ],
        )
        return self.dialog
