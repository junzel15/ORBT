import flet as ft
from flet import UserControl
from pages.chat import stream_chat
import asyncio


class NewMessagePage(UserControl):
    def __init__(self, page: ft.Page, go_to):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.contacts_column = ft.Column()

        self.page.title = "New Message"
        self.page.padding = 0
        self.page.scroll = "adaptive"
        self.page.bgcolor = "#F8F9FA"

        self.header_section = ft.Container(
            content=ft.Row(
                [
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        icon_size=24,
                        on_click=lambda e: self.go_to("/messages", self.page),
                    ),
                    ft.Text("New Message", size=18, weight="bold"),
                ],
                alignment="start",
                vertical_alignment="center",
            ),
            padding=15,
        )

        self.search_section = ft.Container(
            content=ft.TextField(
                hint_text="Search contacts",
                prefix_icon=ft.icons.SEARCH,
                on_change=self.filter_contacts,
                expand=True,
                border_radius=5,
            ),
            padding=15,
        )

        self.contacts_section = ft.Container(content=self.contacts_column, padding=15)

        self.main_content = ft.ListView(
            controls=[
                self.header_section,
                self.search_section,
                self.contacts_section,
            ],
            expand=True,
            padding=ft.padding.all(16),
        )

        asyncio.run(self.load_contacts())

    async def load_contacts(self):
        # THIS IS A TEMPORARY CONTACT SIR DYLAN.
        contacts = [
            {"id": "1", "name": "Sir CJ"},
            {"id": "2", "name": "Sir Dylan"},
            {"id": "3", "name": "Sir Paul"},
        ]

        self.contacts_column.controls.clear()

        for contact in contacts:
            self.contacts_column.controls.append(
                self.contact_item(contact["id"], contact["name"])
            )

        self.page.update()

    # This function if have a stored contact in stream
    # async def load_contacts(self):
    #     contacts = await asyncio.to_thread(stream_chat.get_contacts)
    #     self.contacts_column.controls.clear()

    #     for contact in contacts:
    #         self.contacts_column.controls.append(
    #             self.contact_item(contact["id"], contact["name"])
    #         )

    #     self.page.update()

    def contact_item(self, user_id, user_name):
        return ft.ListTile(
            leading=ft.Icon(ft.icons.PERSON, size=40, color="#6200EE"),
            title=ft.Text(user_name, weight="bold"),
            on_click=lambda e: self.start_conversation(user_id, user_name),
        )

    def start_conversation(self, user_id, user_name):
        self.go_to(
            "/conversation",
            page=self.page,
            channel_id=user_id,
            contact_name=user_name,
        )

    def filter_contacts(self, e):
        search_text = e.control.value.lower()
        for item in self.contacts_column.controls:
            item.visible = search_text in item.title.value.lower()
        self.page.update()

    def build(self):
        return ft.Column(
            [
                ft.Container(content=self.main_content, expand=True),
                ft.Container(
                    alignment=ft.alignment.bottom_center,
                    bgcolor="#FFFFFF",
                    padding=ft.padding.all(10),
                ),
            ]
        )
