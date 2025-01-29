import flet as ft
import calendar
import datetime
import json
import os


class BirthdayPage(ft.UserControl):
    def __init__(self, page, go_to, user_id):
        super().__init__()
        self.go_to = go_to
        self.page = page
        self.user_id = str(user_id)
        self.year = 1990
        self.month = 9
        self.day = 12
        self.selected_date_text = ft.Text(
            f"{self.month:02}/{self.day:02}/{self.year}",
            font_family="Sora-Regular",
            color=ft.Colors.WHITE,
        )
        self.day_grid_container = None

    def save_birthday(self):
        """Save selected birthday to users.json for the given user_id."""
        user_birthday = f"{self.year}-{self.month:02}-{self.day:02}"
        print(f"Attempting to save birthday for user_id: {self.user_id}")

        data = []
        if os.path.exists("users.json"):
            with open("users.json", "r") as file:
                try:
                    data = json.load(file)
                    if not isinstance(data, list):
                        data = []
                except json.JSONDecodeError:
                    print(
                        "Error: users.json is corrupted or empty. Initializing as empty list."
                    )
                    data = []

        print("Current users.json content before update:", data)

        user_found = False
        for user in data:
            if str(user.get("id")) == self.user_id:
                print(f"Updating birthday for user {self.user_id}")
                user["birthday"] = user_birthday
                user_found = True
                break

        if not user_found:
            print(f"User with ID {self.user_id} not found. Adding new user entry.")
            new_user = {"id": self.user_id, "birthday": user_birthday}
            data.append(new_user)

        with open("users.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Updated users.json content:", data)

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        expand=1,
                        height=600,
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    ft.Row(
                                        controls=[
                                            ft.CupertinoButton(
                                                alignment=ft.Alignment(-1, 0),
                                                content=ft.Image(
                                                    src="images/back_white.png",
                                                    width=22,
                                                    height=22,
                                                    fit=ft.ImageFit.FILL,
                                                ),
                                                on_click=lambda e: self.go_to(
                                                    "/gender", self.page
                                                ),
                                            ),
                                            ft.Container(width=20),
                                            ft.ProgressBar(
                                                width=197,
                                                color="#A87AFE",
                                                bgcolor="#E4DFDF",
                                                value=2 / 5,
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
                                                    height=450,
                                                    controls=[
                                                        ft.Text(
                                                            "When is your birthday?",
                                                            font_family="Sora-SemiBold",
                                                            size=20,
                                                            text_align=ft.TextAlign.CENTER,
                                                            color=ft.Colors.WHITE,
                                                            weight=ft.FontWeight.W_700,
                                                            width=300,
                                                        ),
                                                        ft.Container(height=10),
                                                        self.create_display_text(),
                                                        ft.Container(height=5),
                                                        ft.Container(
                                                            height=314,
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.Container(
                                                                        height=5
                                                                    ),
                                                                    self.create_month_year_dropdowns(),
                                                                    self.create_day_grid(),
                                                                ],
                                                            ),
                                                            border_radius=10,
                                                            border=ft.border.all(
                                                                1, "#DFDFE4"
                                                            ),
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
                            ],
                        ),
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
                    ft.Container(height=2),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.TextButton(
                                    "Skip for now",
                                    style=ft.ButtonStyle(
                                        text_style=ft.TextStyle(
                                            font_family="InstrumentSans-Regular",
                                            size=16,
                                            color=ft.Colors.WHITE,
                                        ),
                                        color=ft.Colors.WHITE,
                                    ),
                                    on_click=lambda e: self.go_to(
                                        "/interest", self.page
                                    ),
                                ),
                            ]
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

    def create_display_text(self):
        return ft.Container(
            width=300,
            height=50,
            content=ft.Row(
                controls=[
                    ft.Image(
                        src="images/icon_calendar.png",
                        width=24,
                        height=24,
                    ),
                    self.selected_date_text,
                ],
            ),
            padding=ft.Padding(20, 0, 20, 0),
            border_radius=10,
            border=ft.border.all(1, "#DFDFE4"),
        )

    def create_month_year_dropdowns(self):
        return ft.Container(
            width=300,
            height=42,
            content=ft.Row(
                controls=[
                    ft.Container(width=10),
                    ft.Dropdown(
                        height=42,
                        alignment=ft.alignment.center,
                        content_padding=ft.Padding(left=20, top=3, right=10, bottom=3),
                        color="#FFFFFF",
                        filled=True,
                        fill_color="#5300FA",
                        border_radius=20,
                        border_width=1,
                        border_color="#FFFFFF",
                        select_icon_enabled_color="#FFFFFF",
                        width=138,
                        value=self.month,
                        bgcolor="#5300FA",
                        item_height=48,
                        text_style=ft.TextStyle(
                            font_family="InstrumentSans-SemiBold",
                            size=14,
                            color=ft.Colors.WHITE,
                        ),
                        options=[
                            ft.dropdown.Option(
                                str(i), str(datetime.date(2022, i, 1).strftime("%B"))
                            )
                            for i in range(1, 13)
                        ],
                        on_change=self.on_month_change,
                        on_click=self.on_dropdown_click,
                    ),
                    ft.Container(width=20),
                    ft.Dropdown(
                        height=42,
                        alignment=ft.alignment.center,
                        content_padding=ft.Padding(left=20, top=3, right=10, bottom=3),
                        color="#FFFFFF",
                        filled=True,
                        fill_color="#5300FA",
                        border_radius=20,
                        border_width=1,
                        border_color="#FFFFFF",
                        select_icon_enabled_color="#FFFFFF",
                        width=92,
                        value=self.year,
                        bgcolor="#5300FA",
                        item_height=48,
                        text_style=ft.TextStyle(
                            font_family="InstrumentSans-Regular",
                            size=14,
                            color=ft.Colors.WHITE,
                        ),
                        options=[
                            ft.dropdown.Option(str(i), str(i))
                            for i in range(1900, datetime.date.today().year + 1)
                        ],
                        on_change=self.on_year_change,
                    ),
                    ft.Container(width=10),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                height=40,
            ),
            padding=ft.Padding(0, 0, 0, 0),
        )

    def create_day_grid(self):
        self.day_grid_container = ft.Container(
            content=self.render_days_grid(),
            padding=ft.Padding(0, 0, 0, 20),
        )
        return self.day_grid_container

    def render_days_grid(self):
        print("render_days_grid")
        first_weekday, num_days = calendar.monthrange(self.year, self.month)
        first_weekday = (first_weekday + 1) % 7

        print("first_weekday: ", first_weekday)
        print("num_days", num_days)

        previous_month = self.month - 1 if self.month > 1 else 12
        previous_year = self.year if self.month > 1 else self.year - 1
        prev_month_days = calendar.monthrange(previous_year, previous_month)[1]

        next_month = self.month + 1 if self.month < 12 else 1
        next_year = self.year if self.month < 12 else self.year + 1

        date_button_width = 35
        date_button_height = 30

        grid = []

        grid.append(
            ft.Row(
                controls=[
                    ft.Container(
                        width=date_button_width,
                        height=date_button_height,
                        bgcolor=ft.Colors.TRANSPARENT,
                        content=ft.Text(
                            day,
                            size=12,
                            color=ft.Colors.WHITE,
                            width=42,
                            text_align=ft.TextAlign.CENTER,
                        ),
                    )
                    for day in ["S", "M", "T", "W", "T", "F", "S"]
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            )
        )

        current_row = [
            ft.TextButton(
                text=str(prev_month_days - first_weekday + d + 1),
                style=ft.ButtonStyle(
                    color="#737373",
                    text_style=ft.TextStyle(color="#737373"),
                    bgcolor=ft.Colors.TRANSPARENT,
                ),
                width=date_button_width,
                height=date_button_height,
            )
            for d in range(first_weekday)
        ]

        for day in range(1, num_days + 1):
            current_row.append(
                ft.TextButton(
                    text=str(day),
                    on_click=lambda e, d=day: self.on_day_select(d),
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        text_style=ft.TextStyle(color=ft.Colors.WHITE),
                        bgcolor=ft.Colors.TRANSPARENT if day != self.day else "#5300FA",
                        shape=ft.RoundedRectangleBorder(radius=5),
                        side={
                            ft.ControlState.DEFAULT: ft.BorderSide(
                                1,
                                ft.Colors.TRANSPARENT if day != self.day else "#5300FA",
                            ),
                        },
                    ),
                    width=date_button_width,
                    height=date_button_height,
                )
            )
            if len(current_row) == 7:
                grid.append(
                    ft.Row(
                        controls=current_row,
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    )
                )
                current_row = []

        next_day = 1
        if current_row:
            while len(current_row) < 7:
                current_row.append(
                    ft.TextButton(
                        text=str(next_day),
                        style=ft.ButtonStyle(
                            color="#737373",
                            text_style=ft.TextStyle(color="#737373"),
                            bgcolor=ft.Colors.TRANSPARENT,
                        ),
                        width=date_button_width,
                        height=date_button_height,
                    )
                )
                next_day += 1
            grid.append(
                ft.Row(
                    controls=current_row, alignment=ft.MainAxisAlignment.SPACE_AROUND
                )
            )

        return ft.Column(
            controls=grid,
            width=300,
            alignment=ft.CrossAxisAlignment.CENTER,
            key="grid_column",
        )

    def on_month_change(self, e):
        self.month = int(e.control.value)
        self.update_calendar()

    def on_dropdown_click(self, e):
        print("on_dropdown_click")

    def on_year_change(self, e):
        self.year = int(e.control.value)
        self.update_calendar()

    def on_day_select(self, day):
        self.day = day
        print("on_day_select: ", day)
        self.update_selected_date()

    def update_selected_date(self):
        self.selected_date_text.value = f"{self.month:02}/{self.day:02}/{self.year}"
        print("self.selected_date_text.value: ", self.selected_date_text.value)
        self.selected_date_text.update()
        self.update_calendar()

    def update_calendar(self):
        self.day_grid_container.content.controls.clear()
        self.day_grid_container.content = self.render_days_grid()
        print(f"Updated content: {self.day_grid_container.content}")
        self.day_grid_container.update()

    def on_next_click(self):
        self.save_birthday()
        self.go_to("/aboutme", self.page)
