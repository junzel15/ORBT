import flet as ft


def form_filled(label, placeholder, is_password=False, icon=None):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(icon) if icon else None,
                        ft.Text(label),
                    ],
                    spacing=5,
                ),
                ft.TextField(
                    hint_text=placeholder,
                    password=is_password,
                ),
            ],
            spacing=5,
        ),
    )
