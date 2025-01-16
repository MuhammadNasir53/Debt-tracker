import flet as ft


def input_field(text):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.TextField(
            height=45,
            width=300,
            text_size=12,
            color="black",
            border_radius=6,
            bgcolor="#f0f3f6",
            border_color="transparent",
            filled=True,
            hint_text=text,
            hint_style=ft.TextStyle(size=11, color="black"),
        ),
    )


def add_debt():
    name = input_field("Name")
    amount = input_field("Amount")
    date = input_field("Date")
    return ft.Column(
        alignment=ft.alignment.center,
        controls=[
            name,
            amount,
            date,
        ]
    )
