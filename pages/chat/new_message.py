import flet as ft
from flet import UserControl
from pages.chat import stream_chat

import boto3


dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
friends_table = dynamodb.Table("friends")


class NewMessagePage(UserControl):
    def __init__(self, page: ft.Page, go_to):
        super().__init__()
        self.page = page
        self.go_to = go_to

        self.page.title = "New Message"
        self.page.scroll = "adaptive"
        self.page.padding = 0
        self.page.bgcolor = "#F8F9FA"

        self.page.window_width = 400
        self.page.window_height = 680
        self.page.update()

        self.header_section = ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        icon_size=24,
                        on_click=lambda e: self.go_to("/messages", self.page),
                    ),
                    ft.Text("New Message", size=18, weight="bold"),
                ],
                alignment="start",
                vertical_alignment="center",
                spacing=10,
            ),
            padding=ft.padding.symmetric(horizontal=15, vertical=10),
        )

        self.search_bar = ft.TextField(
            hint_text="Type a name or group",
            prefix_icon=ft.icons.SEARCH,
            border_radius=8,
            expand=True,
        )

        self.group_chat_section = ft.ListTile(
            leading=ft.CircleAvatar(
                content=ft.Icon(ft.icons.GROUP),
                radius=20,
            ),
            title=ft.Text("Group Chat", weight="bold"),
            on_click=lambda e: self.go_to("/groupchat", self.page),
        )

        self.contacts_section = ft.Column()

        self.content = ft.Column(
            controls=[
                self.header_section,
                ft.Container(
                    content=self.search_bar, padding=ft.padding.symmetric(horizontal=15)
                ),
                ft.Container(
                    content=self.group_chat_section,
                    padding=ft.padding.symmetric(horizontal=15),
                ),
                ft.Container(
                    content=ft.Text("Suggested", size=16, weight="bold"),
                    padding=ft.padding.symmetric(horizontal=15, vertical=5),
                ),
                self.contacts_section,
            ],
            expand=True,
        )

        self.refresh_contacts()

    def contact_item(self, contact):
        return ft.ListTile(
            leading=ft.CircleAvatar(
                content=ft.Text(contact["name"][0].upper()),
                radius=20,
            ),
            title=ft.Text(contact["name"], weight="bold"),
            on_click=lambda e, c=contact: self.start_direct_message(c["id"], c["name"]),
        )

    def start_direct_message(self, contact_id, contact_name):
        try:
            channel_id = f"dm_{contact_id}"
            user_id, _ = stream_chat.get_authenticated_user()

            if not user_id:
                print("Error: User ID not found.")
                return

            stream_chat.chat_client.upsert_user(
                {"id": contact_id, "name": contact_name}
            )

            channel = stream_chat.chat_client.channel(
                "messaging",
                channel_id,
                {"members": [user_id, contact_id], "created_by": {"id": user_id}},
            )
            channel.create(user_id)

            self.go_to(
                "/conversation",
                self.page,
                channel_id=channel_id,
                contact_name=contact_name,
            )
        except Exception as e:
            print(f"Error starting direct message: {e}")

    def refresh_contacts(self):
        try:
            self.user_id, self.token = stream_chat.get_authenticated_user()
        except ValueError:
            self.user_id, self.token = None, None

        self.suggested_contacts = self.get_direct_messages()
        self.contacts_section.controls = [
            self.contact_item(contact) for contact in self.suggested_contacts
        ]
        self.page.update()

    def get_direct_messages(self):
        if not self.user_id:
            return []

        try:
            response = friends_table.scan()
            contacts = response.get("Items", [])

            return [
                {"id": contact["friend_id"], "name": contact["name"]}
                for contact in contacts
            ]
        except Exception as e:
            print(f"Error fetching contacts from DynamoDB: {e}")
            return []

    def build(self):
        return self.content
