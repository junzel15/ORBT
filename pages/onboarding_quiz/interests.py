import flet as ft
import json
import os


class InterestPage(ft.UserControl):
    def __init__(self, page, go_to):
        super().__init__()
        self.go_to = go_to
        self.page = page
        self.selected_interests = set()
        self.suggestions = [
            "Films",
            "Concerts",
            "Food",
            "Sports",
            "Art",
            "Travels",
            "Cooking",
            "Plants",
            "Coffee",
        ]
        self.filtered_suggestions = self.suggestions.copy()

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.CupertinoButton(
                                    content=ft.Image(
                                        src="images/back_white.png",
                                        width=22,
                                        height=22,
                                    ),
                                    on_click=lambda e: self.go_to(
                                        "/aboutme", self.page
                                    ),
                                ),
                                ft.Container(width=20),
                                ft.ProgressBar(
                                    width=197,
                                    color="#A87AFE",
                                    bgcolor="#E4DFDF",
                                    value=5 / 5,
                                ),
                            ],
                        ),
                        padding=ft.Padding(0, 0, 50, 0),
                    ),
                    ft.Container(
                        width=1000,
                        height=540,
                        content=ft.Stack(
                            controls=[
                                ft.Image(
                                    src="images/stack_card.png",
                                    width=332,
                                    height=540,
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Text(
                                                "Let us know what you're passionate about!",
                                                font_family="Sora-SemiBold",
                                                size=20,
                                                color=ft.Colors.WHITE,
                                                weight=ft.FontWeight.W_700,
                                                text_align=ft.TextAlign.CENTER,
                                            ),
                                            ft.Container(
                                                content=ft.TextField(
                                                    hint_text="Add your interests",
                                                    on_change=self.on_search_change,
                                                    height=40,
                                                    bgcolor=ft.Colors.WHITE,
                                                    text_style=ft.TextStyle(
                                                        font_family="InstrumentSans-Regular",
                                                        size=14,
                                                    ),
                                                    content_padding=ft.Padding(
                                                        10, 5, 10, 5
                                                    ),
                                                    border_radius=ft.border_radius.all(
                                                        8
                                                    ),
                                                ),
                                                padding=ft.Padding(0, 10, 0, 20),
                                            ),
                                            ft.Container(
                                                content=self.build_wrapping_buttons(
                                                    max_width=300
                                                ),
                                                padding=ft.padding.all(10),
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                    ),
                                    padding=ft.Padding(20, 30, 20, 0),
                                ),
                            ],
                        ),
                        padding=ft.Padding(20, 0, 20, 0),
                    ),
                    ft.Container(height=7),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.ElevatedButton(
                                    width=1000,
                                    height=50,
                                    text="Next",
                                    style=ft.ButtonStyle(
                                        text_style=ft.TextStyle(
                                            font_family="InstrumentSans-SemiBold",
                                            size=16,
                                            color=ft.Colors.WHITE,
                                        ),
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                    ),
                                    color=ft.Colors.WHITE,
                                    bgcolor="#5300FA",
                                    on_click=lambda e: self.on_next_click(),
                                ),
                            ]
                        ),
                        alignment=ft.alignment.top_center,
                        padding=ft.Padding(20, 0, 20, 0),
                    ),
                    ft.Container(
                        content=ft.TextButton(
                            "Skip for now",
                            style=ft.ButtonStyle(
                                text_style=ft.TextStyle(
                                    font_family="InstrumentSans-Regular",
                                    size=16,
                                    color=ft.Colors.WHITE,
                                ),
                                color=ft.Colors.WHITE,
                            ),
                            on_click=lambda e: self.go_to("/notification-", self.page),
                        ),
                        alignment=ft.alignment.top_center,
                        padding=ft.Padding(20, 0, 20, 0),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            padding=ft.Padding(20, 0, 20, 10),
            expand=1,
            alignment=ft.alignment.top_center,
            bgcolor=ft.Colors.BLACK,
        )

    def create_interest_button(self, interest):
        """Create a button for an interest."""
        is_selected = interest in self.selected_interests
        estimated_width = min(150, len(interest) * 10 + 25)

        suffix_text = "✓" if is_selected else "+"

        return ft.Container(
            content=ft.ElevatedButton(
                text=f"{interest} {suffix_text}",
                style=ft.ButtonStyle(
                    bgcolor=(
                        ft.Colors.WHITE
                        if is_selected
                        else ft.colors.with_opacity(0.15, "#5300FA")
                    ),
                    text_style=ft.TextStyle(
                        font_family=(
                            "InstrumentSans-SemiBold"
                            if is_selected
                            else "InstrumentSans-Regular"
                        ),
                        size=14,
                        color="#5300FA" if is_selected else ft.Colors.WHITE,
                    ),
                    color="#5300FA" if is_selected else ft.Colors.WHITE,
                    shape=ft.RoundedRectangleBorder(radius=20),
                    side={
                        ft.ControlState.DEFAULT: ft.BorderSide(
                            1, ft.Colors.TRANSPARENT if is_selected else "#5300FA"
                        ),
                    },
                ),
                on_click=lambda _: self.toggle_interest(interest),
            ),
            width=estimated_width,
            margin=ft.margin.all(2),
        )

    def build_wrapping_buttons(self, max_width=300):
        """Dynamically creates rows of buttons that wrap based on available width."""
        current_row = []
        rows = []
        current_width = 0

        for interest in self.filtered_suggestions:
            estimated_width = min(150, len(interest) * 10 + 10) + 10
            if current_width + estimated_width > max_width:
                rows.append(ft.Row(controls=current_row, spacing=5))
                current_row = []
                current_width = 0
            current_row.append(self.create_interest_button(interest))
            current_width += estimated_width

        if current_row:
            rows.append(ft.Row(controls=current_row, spacing=5))

        return ft.Column(controls=rows, spacing=10)

    def toggle_interest(self, interest):
        """Toggle the selection of an interest."""
        if interest in self.selected_interests:
            self.selected_interests.remove(interest)
        else:
            self.selected_interests.add(interest)
        self.update_screen()

    def on_search_change(self, event):
        """Filter suggestions based on search input."""
        query = event.control.value.lower()
        self.filtered_suggestions = [
            interest for interest in self.suggestions if query in interest.lower()
        ]
        self.update_screen()

    def update_screen(self):
        """Update the screen dynamically."""
        try:
            self.controls[0].content.controls[1].content.controls[1].content.controls[
                2
            ].content = self.build_wrapping_buttons(max_width=300)
            self.update()
        except IndexError as e:
            print(
                f"IndexError: {e}. Unable to update screen due to wrong index access."
            )

    def on_next_click(self):
        """Save selected interests and navigate to the next page."""
        self.save_interests()
        self.go_to("/location", self.page)

    def save_interests(self):
        """Save selected interests to users.json."""
        if os.path.exists("users.json"):
            with open("users.json", "r") as file:
                try:
                    data = json.load(file)
                    if not isinstance(data, list):
                        data = []
                except json.JSONDecodeError:
                    data = []
        else:
            data = []

        if data:
            data[0]["interests"] = list(self.selected_interests)

        with open("users.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Interests saved:", self.selected_interests)
