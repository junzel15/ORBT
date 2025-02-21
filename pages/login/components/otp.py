import flet as ft
import json


class OtpPage(ft.UserControl):
    def __init__(self, page, go_to):
        super().__init__()
        self.go_to = go_to
        self.page = page
        self.text_fields = []
        self.verify_button = None
        self.entered_otp = ""

        self.page.window_width = 380
        self.page.window_height = 680
        self.page.update()

    def build(self):
        def create_text_field(index):

            def on_focus(event):
                event.control.border_color = "#5300FA"
                if event.control.value == "-":
                    event.control.value = ""
                event.control.update()

            def on_change(event):
                if len(event.control.value) > 1:
                    event.control.value = event.control.value[-1]
                if event.control.value.isdigit() and index < len(self.text_fields) - 1:
                    self.text_fields[index + 1].focus()
                validate_inputs()
                event.control.update()

            text_field = ft.TextField(
                width=65,
                height=65,
                text_align=ft.TextAlign.CENTER,
                border_color="#DFDFE4",
                border_radius=ft.border_radius.all(8),
                keyboard_type=ft.KeyboardType.NUMBER,
                text_style=ft.TextStyle(
                    font_family="Sora-Regular",
                    size=24,
                ),
                value="-",
                on_focus=on_focus,
                on_change=on_change,
            )
            self.text_fields.append(text_field)
            return text_field

        def validate_inputs():
            all_filled = all(field.value.isdigit() for field in self.text_fields)
            if all_filled:
                self.verify_button.bgcolor = "#5300FA"
                self.verify_button.disabled = False
            else:
                self.verify_button.bgcolor = "#A2A8BF"
                self.verify_button.disabled = True
            self.verify_button.update()

        self.verify_button = ft.ElevatedButton(
            width=1000,
            height=50,
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(
                            value="Verify",
                            font_family="InstrumentSans-SemiBold",
                            size=16,
                            color="#FFFFFF",
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                padding=ft.padding.all(10),
            ),
            bgcolor="#A2A8BF",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
            ),
            on_click=self.on_verify_click,
            disabled=True,
        )

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.CupertinoButton(
                                alignment=ft.Alignment(-1, 0),
                                content=ft.Image(
                                    src="images/back.png",
                                    width=22,
                                    height=22,
                                    fit=ft.ImageFit.FILL,
                                ),
                                on_click=self.on_back_click,
                            ),
                            ft.Container(width=1000),
                        ],
                    ),
                    ft.Container(
                        padding=ft.Padding(20, 0, 0, 0),
                        content=ft.Text(
                            "Verification",
                            font_family="Sora-SemiBold",
                            size=20,
                            color="#000000",
                        ),
                    ),
                    ft.Container(
                        padding=ft.Padding(20, 0, 0, 0),
                        content=ft.Text(
                            "We’ve sent you the verification code to\n+63 964 201 ****",
                            font_family="InstrumentSans-Regular",
                            size=14,
                            text_align=ft.TextAlign.START,
                        ),
                    ),
                    ft.Container(height=20),
                    ft.Row(
                        spacing=30,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            create_text_field(0),
                            create_text_field(1),
                            create_text_field(2),
                            create_text_field(3),
                        ],
                    ),
                    ft.Container(height=20),
                    ft.Container(
                        padding=ft.Padding(20, 0, 0, 0),
                        content=self.verify_button,
                    ),
                    ft.Container(height=10),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "Re-send code in ",
                                font_family="InstrumentSans-Regular",
                                size=14,
                            ),
                            ft.Text(
                                "0:20",
                                font_family="InstrumentSans-Regular",
                                size=14,
                                color=ft.Colors.BLUE,
                                weight="bold",
                            ),
                        ],
                    ),
                    ft.Container(height=1000),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            expand=True,
            alignment=ft.alignment.top_center,
            bgcolor=ft.Colors.WHITE,
            padding=ft.Padding(0, 0, 20, 10),
        )

    def on_back_click(self, _):
        print("Back Click")
        self.page.go("/forgotpassword")

    def on_verify_click(self, _):
        print("Verify Click")
        self.page.go("/resetpassword")

        def on_verify_click(self, _):

            with open("json/users.json", "r") as file:
                users = json.load(file)

            otp_verified = False
            for user in users:
                if user["otp"]["reset_password"] == self.entered_otp:
                    otp_verified = True
                    break

            if otp_verified:
                print("OTP Verified")
                self.go_to("/resetpassword", self.page)
            else:
                print("Invalid OTP")

        return ft.Column(
            controls=[...],
            spacing=10,
        )

    def on_change(self, event):
        self.entered_otp = "".join([field.value for field in self.text_fields])
        self.update()
