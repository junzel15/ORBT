import flet as ft
from flet import UserControl
from pages.chat import stream_chat


class GroupChatPages(UserControl):
    def __init__(self, page: ft.Page, go_to):
        super().__init__()
        self.page = page
        self.go_to = go_to
        self.selected_users = []
        self.contacts_section = ft.Column()

        self.page.title = "New Group"
        self.page.scroll = "adaptive"
        self.page.padding = 0
        self.page.bgcolor = "#F8F9FA"

        self.header_section = ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        icon_size=24,
                        on_click=lambda e: self.go_to("/messages", self.page),
                    ),
                    ft.Text("New Group", size=18, weight="bold"),
                ],
                alignment="start",
                vertical_alignment="center",
                spacing=10,
            ),
            padding=ft.padding.symmetric(horizontal=15, vertical=10),
        )

        self.group_name_field = ft.TextField(
            hint_text="Enter Group Name",
            border_radius=8,
            expand=True,
            on_change=self.update_create_button_state,
        )

        self.search_section = ft.TextField(
            hint_text="Search",
            prefix_icon=ft.icons.SEARCH,
            border_radius=8,
            expand=True,
        )

        self.create_button = ft.ElevatedButton(
            text="Create Group Chat",
            bgcolor="lightblue",
            color="white",
            disabled=True,
            on_click=self.create_new_group_chat,
            style=ft.ButtonStyle(
                bgcolor={
                    "": "lightblue",
                    "hovered": "darkblue",
                },
            ),
        )

        self.content = ft.Column(
            controls=[
                self.header_section,
                ft.Container(
                    content=self.group_name_field,
                    padding=ft.padding.symmetric(horizontal=15),
                ),
                ft.Container(
                    content=self.search_section,
                    padding=ft.padding.symmetric(horizontal=15),
                ),
                ft.Container(
                    content=ft.Text("Suggested", size=16, weight="bold"),
                    padding=ft.padding.symmetric(horizontal=15, vertical=5),
                ),
                self.contacts_section,
                ft.Container(
                    content=self.create_button,
                    padding=ft.padding.all(15),
                    alignment=ft.alignment.center,
                ),
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
            trailing=ft.Checkbox(
                value=False,
                on_change=lambda e, c=contact: self.toggle_selection(
                    c, e.control.value
                ),
            ),
        )

    def toggle_selection(self, contact, selected):
        if selected:
            self.selected_users.append(contact)
        else:
            self.selected_users.remove(contact)

        self.update_create_button_state()

    def update_create_button_state(self, e=None):
        group_name_entered = bool(self.group_name_field.value.strip())
        has_selected_users = len(self.selected_users) > 0

        self.create_button.disabled = not (group_name_entered and has_selected_users)
        self.create_button.update()

    def create_new_group_chat(self, e):
        if not self.selected_users or not self.group_name_field.value.strip():
            return

        group_name = self.group_name_field.value.strip()
        channel_id = f"group_{'_'.join(user['id'] for user in self.selected_users)}"

        print(f"Creating group: {group_name} with users {self.selected_users}")

        self.go_to("/conversation", self.page, channel_id=channel_id)

    def refresh_contacts(self):

        try:
            self.user_id, self.token = stream_chat.get_authenticated_user()
        except ValueError:
            self.user_id, self.token = None, None

        self.suggested_contacts = self.get_group_messages()

        print("Loaded contacts:", self.suggested_contacts)

        self.contacts_section.controls.clear()
        for contact in self.suggested_contacts:
            self.contacts_section.controls.append(self.contact_item(contact))

        self.update()  # Ensure UI updates

    def get_group_messages(self):
        # TEMPORARY CONTACT
        return [
            {"id": "test_one", "name": "Test One"},
            {"id": "test_two", "name": "Test Two"},
            {"id": "test_three", "name": "Test Three"},
        ]

    def build(self):
        return self.content
