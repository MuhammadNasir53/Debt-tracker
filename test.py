import flet as ft

# Gradient for styling containers
COLOR = ft.LinearGradient(
    begin=ft.alignment.top_left,
    end=ft.alignment.bottom_right,
    colors=["green", "blue", "green"],
)

def main(page: ft.Page):
    # Set up the page properties
    page.window.width = 380
    page.window.height = 840
    page.title = "Debt Tracker App"
    page.padding = 10
    page.scroll = "auto"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Welcome Section
    welcome_section = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Welcome to", size=18, weight="bold", color=ft.colors.GREY_800),
                ft.Text("Debt Tracker", size=24, weight="bold", color=ft.colors.BLUE),
                ft.Text(
                    "Track, manage, and pay off your debts with ease!",
                    size=14,
                    color=ft.colors.GREY_600,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=15,
        border_radius=10,
        gradient=COLOR,
    )

    # Debt Overview Section
    debt_summary = ft.Row(
        controls=[
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Total Debt", weight="bold", size=16),
                        ft.Text("₦2500", size=20, weight="bold", color=ft.colors.RED),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=15,
                border_radius=10,
                bgcolor=ft.colors.RED_100,
                width=140,
                height=100,
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Paid Debt", weight="bold", size=16),
                        ft.Text("₦1500", size=20, weight="bold", color=ft.colors.GREEN),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=15,
                border_radius=10,
                bgcolor=ft.colors.GREEN_100,
                width=140,
                height=100,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    # Action Buttons Section
    action_buttons = ft.Row(
        controls=[
            ft.ElevatedButton(
                "Add New Debt",
                icon=ft.icons.ADD,
                bgcolor=ft.colors.BLUE,
                color=ft.colors.WHITE,
            ),
            ft.ElevatedButton(
                "Pay Off Debt",
                icon=ft.icons.MONEY,
                bgcolor=ft.colors.GREEN,
                color=ft.colors.WHITE,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        spacing=20,
    )

    # Recent Debts Section
    recent_debts = ft.Column(
        controls=[
            ft.Text("Recent Debts", size=16, weight="bold"),
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text("Mumini", size=14),
                        ft.Text("₦250 - 01/10/2025", size=14, weight="bold"),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                padding=10,
                border_radius=5,
                bgcolor=ft.colors.GREY_100,
            ),
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text("Musa", size=14),
                        ft.Text("₦400 - 02/10/2025", size=14, weight="bold"),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                padding=10,
                border_radius=5,
                bgcolor=ft.colors.GREY_100,
            ),
            ft.TextButton("See All", icon=ft.icons.LIST),
        ],
        spacing=10,
    )

    # Floating Action Button
    floating_button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        bgcolor=ft.colors.BLUE,
        tooltip="Quick Add Debt",
    )

    # Add everything to the page
    page.add(
        welcome_section,
        ft.Divider(),
        debt_summary,
        ft.Divider(),
        action_buttons,
        ft.Divider(),
        recent_debts,
        floating_button,
    )


ft.app(target=main)
