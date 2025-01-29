import flet as ft


class CustomTextField(ft.UserControl):
    def __init__(
        self,
        hint_text,
        left_icon=None,
        right_icon=None,
        left_image=None,
        is_password=False,
    ):
        super().__init__()
        self.hint_text = hint_text
        self.left_icon = left_icon
        self.right_icon = right_icon
        self.left_image = left_image
        self.is_password = is_password
        self.text_field = ft.TextField(
            hint_text=self.hint_text,
            password=self.is_password,
            border_color=ft.Colors.TRANSPARENT,
            expand=True,
        )

    @property
    def value(self):
        return self.text_field.value

    def build(self):
        def toggle_password_visibility(e):
            self.is_password = not self.is_password
            self.text_field.password = self.is_password
            self.update()

        controls = [ft.Container(width=10)]

        if self.left_icon:
            controls.append(ft.Icon(self.left_icon, color=ft.Colors.GREY_500, size=24))

        if self.left_image:
            controls.append(
                ft.Image(
                    src=self.left_image,
                    width=22,
                    height=22,
                    fit=ft.ImageFit.FILL,
                )
            )

        controls.append(self.text_field)

        if self.right_icon:
            controls.append(
                ft.IconButton(
                    icon=self.right_icon,
                    icon_color=ft.Colors.GREY_500,
                    height=50,
                    width=24,
                    on_click=toggle_password_visibility,
                )
            )

        controls.append(ft.Container(width=10))

        return ft.Container(
            border=ft.border.all(1, ft.Colors.GREY_300),
            border_radius=ft.border_radius.all(10),
            content=ft.Row(
                controls=controls,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            height=50,
        )
