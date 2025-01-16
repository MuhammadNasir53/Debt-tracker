import flet as ft
from app.frontend.forms import add_debt

COLOR = ft.LinearGradient(
    begin=ft.alignment.top_left,
    end=ft.alignment.bottom_right,
    colors=["green", "blue", "green"],
)


def add_debt_view(page):
    page.views.clear()
    page.views.append(
        ft.View(
            controls=[
                add_debt()
            ]
        )
    )
    page.update()


def main_ui(page):

    Tittle = ft.Column(
        [
            ft.Column(
                [
                    ft.Text("Welcome", size=30, weight="bold"),
                    ft.Text("Debt Tracker", size=25, weight="bold"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ]
    )

    balance = ft.Container(
        width=350,
        height=55,
        border_radius=10,
        bgcolor="green",
        padding=15,
        expand=True,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text("\u20a6" + "280", size=20, color="white"),
                ft.Container(
                    width=60,
                    height=45,
                    border_radius=5,
                    bgcolor="yellow",
                    alignment=ft.alignment.center,
                    content=ft.Text("Details", size=12, weight="bold"),
                ),
            ],
        ),
    )

    two_con = ft.Row(
        [
            ft.Container(
                width=148,
                height=100,
                border_radius=10,
                bgcolor="green",
                expand=True,
                on_click=lambda _: add_debt_view(page),  # Synchronous handler
            ),
            ft.Container(
                width=148, height=100, border_radius=10, bgcolor="green", expand=True
            ),
        ]
    )

    recent_debt = ft.Column(
        height=300,
        # for the ListView of debt list
    )

    actions = ft.Stack(
        controls=[
            ft.Row(
                [
                    ft.Container(
                        width=40,
                        height=40,
                        border_radius=20,
                        bgcolor="green",
                        alignment=ft.alignment.center,
                        content=ft.Text("+", size=30, weight="bold", color="yellow"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.END,
            ),
        ]
    )

    return ft.Column(
        controls=[
            Tittle,
            balance,
            two_con,
            ft.Text("Recent", size=20, weight="bold"),
            recent_debt,
            actions,
        ]
    )
