import flet as ft
from flet import UserControl
from pages.chat import stream_chat
import asyncio
import boto3
from botocore.exceptions import ClientError
from global_state import get_logged_in_user


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
        contacts = self.get_contacts_from_dynamodb()
        self.contacts_column.controls.clear()

        for contact in contacts:
            self.contacts_column.controls.append(
                self.contact_item(contact["id"], contact["name"])
            )

        self.contacts_column.controls.append(
            ft.ListTile(
                leading=ft.Icon(ft.icons.GROUP_ADD, size=40, color="#6200EE"),
                title=ft.Text("New Group Chat", weight="bold"),
                on_click=lambda e: self.create_new_group_chat(),
            )
        )

        self.page.update()

    def get_contacts_from_dynamodb(self):
        dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
        table = dynamodb.Table("profiles")
        user_email = get_logged_in_user()["email"]

        try:
            response = table.get_item(Key={"email": user_email})
            friends = response.get("Item", {}).get("friends", [])

            contacts = []
            for friend_email in friends:
                friend_response = table.get_item(Key={"email": friend_email})
                friend_item = friend_response.get("Item", {})
                contacts.append(
                    {"id": friend_email, "name": friend_item.get("full_name", "Friend")}
                )

            return contacts
        except ClientError as e:
            print("Error fetching contacts from DynamoDB:", e)
            return []

    def create_new_group_chat(self):
        group_name = self.get_group_name_from_user()
        if not group_name:
            print("Group creation canceled.")
            return

        group_id = stream_chat.create_group(group_name)
        if not group_id:
            print("Failed to create group on Stream.")
            return

        selected_friend_emails = self.select_friends_from_contacts()
        if not selected_friend_emails:
            print("No friends selected. Group creation canceled.")
            return

        for friend_email in selected_friend_emails:
            success = stream_chat.add_member_to_group(group_id, friend_email)
            if success:
                self.update_dynamodb_group_membership(group_id, friend_email)

        self.go_to(
            f"/conversation?channel_id={group_id}&group_name={group_name}", self.page
        )

    def get_group_name_from_user(self):
        group_name = input("Enter the name for the new group: ")
        return group_name

    def select_friends_from_contacts(self):
        contacts = self.get_contacts_from_dynamodb()
        selected_friend_emails = []
        for contact in contacts:
            if self.is_selected_by_user(contact):
                selected_friend_emails.append(contact["id"])
        return selected_friend_emails

    def is_selected_by_user(self, contact):
        return True

    def update_dynamodb_group_membership(self, group_id, friend_email):
        dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
        table = dynamodb.Table("profiles")

        try:
            response = table.update_item(
                Key={"email": friend_email},
                UpdateExpression="SET group_memberships = list_append(if_not_exists(group_memberships, :empty_list), :new_group)",
                ExpressionAttributeValues={":new_group": [group_id], ":empty_list": []},
            )
            print("DynamoDB updated successfully:", response)
        except ClientError as e:
            print("Error updating DynamoDB:", e)

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
