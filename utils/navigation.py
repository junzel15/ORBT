import flet as ft
from utils.navigation import go_to


def main(page: ft.Page):

    page.title = "ORBT"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.on_route_change = lambda _: go_to(page, page.route)

    go_to(page, "/splash")


ft.app(target=main)
