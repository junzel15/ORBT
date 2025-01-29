import flet as ft


class CountryPhoneCodeSelector(ft.UserControl):
    def __init__(self, countries):
        super().__init__()

        self.countries = sorted(countries, key=lambda c: c["name"])
        self.default_country = self.countries[0]

    def build(self):

        self.phone_code = ft.TextField(
            read_only=False,
            width=150,
            height=50,
            border=ft.InputBorder.NONE,
            keyboard_type=ft.KeyboardType.PHONE,
            hint_text="Enter phone number...",
        )

        self.country_dropdown = ft.Dropdown(
            content_padding=ft.Padding(left=2, top=2, right=2, bottom=2),
            select_icon_enabled_color="#A2A8BF",
            border_width=0,
            width=100,
            height=50,
            value=self.default_country["dial_code"],
            options=[
                ft.dropdown.Option(
                    content=ft.Row(
                        controls=[
                            ft.Image(
                                src=f"{country['image']}",
                                width=30,
                                height=20,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Container(width=8),
                            ft.Text(
                                f"{country['dial_code']}",
                                size=14,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    key=country["dial_code"],
                )
                for country in self.countries
            ],
            on_change=self.on_country_selected,
        )

        return ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=self.country_dropdown, padding=ft.padding.all(0)
                    ),
                    ft.Container(
                        width=1,
                        border=ft.border.only(
                            ft.BorderSide(1, "#DFDFE4"), None, None, None
                        ),
                    ),
                    ft.Container(content=self.phone_code, padding=ft.padding.all(0)),
                ],
                alignment="start",
            ),
            border_radius=10,
            border=ft.border.all(1, "#DFDFE4"),
            height=50,
        )

    def on_country_selected(self, e):
        selected_country_code = e.control.value
        print("Selected country code:", selected_country_code)
        self.phone_code.value = selected_country_code
        self.update()
