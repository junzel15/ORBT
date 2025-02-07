import flet as ft
from pages.mybookings.booking_navbar.components import BookingCard, Tabs, FilterModal
from pages.mybookings.booking_navbar.helpers import filter_bookings


class Bookings(ft.UserControl):
    def __init__(self, page=None, go_to=None, **kwargs):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.current_tab = "Upcoming"
        self.bookings = self.load_bookings()
        self.filter_modal = FilterModal(self.apply_filter)
        self.bookings_list = ft.Column()

    def load_bookings(self):
        return [
            {
                "id": 1,
                "title": "Dining 🍽️",
                "status": "Upcoming",
                "time": "12:30 PM",
                "location": "ABC Restaurant",
            },
            {
                "id": 2,
                "title": "Brew & Co.",
                "status": "Completed",
                "time": "6:00 PM",
                "location": "Brewery Bar",
            },
            {
                "id": 3,
                "title": "The Botchke Bar",
                "status": "Cancelled",
                "time": "9:00 PM",
                "location": "Downtown",
            },
        ]

    def apply_filter(self, filters):
        print("Filters applied:", filters)
        self.bookings = filter_bookings(self.load_bookings(), filters)
        self.update_bookings_list()

    def build(self):
        self.tabs = Tabs(self.switch_tab)

        return ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.icons.ARROW_BACK,
                                        icon_color="#000000",
                                        on_click=lambda _: self.go_to(
                                            "/home", self.page
                                        ),
                                    ),
                                    ft.Text(
                                        "My Bookings",
                                        size=20,
                                        weight="bold",
                                        expand=True,
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.FILTER_LIST,
                                        icon_color="#000000",
                                        on_click=lambda _: self.filter_modal.open(),
                                    ),
                                ],
                            ),
                            ft.Container(
                                content=ft.TextField(
                                    hint_text="Search Events, Dates, Places ...",
                                    prefix_icon=ft.icons.SEARCH,
                                ),
                                padding=ft.padding.only(bottom=10),
                            ),
                            self.tabs,
                            ft.Container(
                                content=self.bookings_list,
                                expand=True,
                            ),
                        ],
                        expand=True,
                    ),
                    expand=True,
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.IconButton(
                                    content=ft.Image(
                                        src="assets/images/Home.png",
                                        width=24,
                                        height=24,
                                    ),
                                    icon_size=24,
                                    icon_color="#000000",
                                    on_click=lambda _: self.go_to("/home", self.page),
                                ),
                            ),
                            ft.Container(
                                content=ft.IconButton(
                                    content=ft.Image(
                                        src="assets/images/Star.png",
                                        width=24,
                                        height=24,
                                    ),
                                    icon_size=24,
                                    icon_color="#000000",
                                    on_click=lambda _: self.go_to(
                                        "/upcoming", self.page
                                    ),
                                ),
                            ),
                            ft.Container(
                                content=ft.IconButton(
                                    content=ft.Image(
                                        src="assets/images/Message.png",
                                        width=24,
                                        height=24,
                                    ),
                                    icon_size=24,
                                    icon_color="#000000",
                                    on_click=lambda _: self.go_to(
                                        "/messages", self.page
                                    ),
                                ),
                            ),
                            ft.Container(
                                content=ft.IconButton(
                                    content=ft.Image(
                                        src="assets/images/Profile.png",
                                        width=24,
                                        height=24,
                                    ),
                                    icon_size=24,
                                    icon_color="#000000",
                                    on_click=lambda _: self.go_to(
                                        "/profile", self.page
                                    ),
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    ),
                    bgcolor="#FFFFFF",
                    border_radius=30,
                    padding=ft.padding.symmetric(vertical=10),
                ),
            ],
            expand=True,
        )

    def switch_tab(self, tab):
        self.current_tab = tab
        self.update_bookings_list()

    def update_bookings_list(self):
        self.bookings_list.controls = [
            BookingCard(booking)
            for booking in self.bookings
            if booking["status"] == self.current_tab
        ]
        self.update()
