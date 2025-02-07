import flet as ft


class BookingCard(ft.UserControl):
    def __init__(self, booking):
        super().__init__()
        self.booking = booking

    def build(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(self.booking["title"], size=16, weight="bold"),
                    ft.Text(f"Time: {self.booking['time']}"),
                    ft.Text(f"Location: {self.booking['location']}"),
                    ft.Row(
                        [
                            ft.ElevatedButton("View Details"),
                            *(
                                [ft.ElevatedButton("Cancel", bgcolor="red")]
                                if self.booking["status"] == "Upcoming"
                                else []
                            ),
                        ]
                    ),
                ]
            ),
            padding=10,
            border_radius=10,
            bgcolor="white",
        )


class Tabs(ft.UserControl):
    def __init__(self, on_tab_change):
        super().__init__()
        self.on_tab_change = on_tab_change

    def build(self):
        return ft.Tabs(
            selected_index=0,
            on_change=lambda e: self.on_tab_change(
                e.control.tabs[e.control.selected_index].text
            ),
            tabs=[
                ft.Tab(text="Upcoming"),
                ft.Tab(text="Completed"),
                ft.Tab(text="Cancelled"),
            ],
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
