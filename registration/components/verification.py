import flet as ft


def verification(label, phone_number):
    def resend_timer():
        resend_button.text = f"Re-send code in 0:{timer.remaining:02d}"
        resend_button.update()

        if timer.remaining == 0:
            resend_button.text = "Re-send code"
            resend_button.disabled = False
            resend_button.update()
            timer.stop()

    def start_resend_timer():
        resend_button.disabled = True
        resend_button.text = "Re-send code in 0:20"
        resend_button.update()
        timer.start()

    def on_verify_click(e):
        print("Verification code submitted")

    back_button = ft.IconButton(
        icon=ft.icons.ARROW_BACK,
        on_click=lambda e: print("Back clicked"),
    )

    inputs = [
        ft.TextField(
            width=60,
            height=60,
            text_align=ft.TextAlign.CENTER,
            border_radius=ft.border_radius.all(8),
            keyboard_type=ft.KeyboardType.NUMBER,
        )
        for _ in range(4)
    ]

    input_row = ft.Row(
        controls=inputs,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    verify_button = ft.ElevatedButton(
        text="Verify",
        width=200,
        height=50,
        on_click=on_verify_click,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=ft.padding.all(10),
        ),
    )

    resend_button = ft.ElevatedButton(
        text="Re-send code in 0:20",
        width=200,
        height=50,
        disabled=True,
        on_click=lambda e: start_resend_timer(),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=ft.padding.all(10),
        ),
    )

    timer = ft.Timer(interval=1000, on_tick=resend_timer)
    timer.remaining = 20

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[back_button],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Text(label, size=24),
                ft.Text(f"Phone number: {phone_number}", size=18, color="gray"),
                input_row,
                verify_button,
                resend_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
        ),
        padding=ft.padding.all(20),
    )
