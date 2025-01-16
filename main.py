import asyncio
import flet as ft
from app.frontend.main_ui import main_ui


async def show_first_view(page):
    page.views.clear()
    page.views.append(
        ft.View(
            controls=[ft.Text("This is the first view. It will change in 3 seconds.")]
        )
    )
    page.update()
    await asyncio.sleep(3)
    show_second_view(page)


def show_second_view(page):
    page.views.clear()
    page.views.append(ft.View(controls=[main_ui(page)]))
    page.update()


def main(page: ft.Page):
    page.window.width = 380
    page.window.height = 840
    page.title = "Debt Tracker App"

    # Run the asynchronous first view function in the main event loop
    asyncio.run(show_first_view(page))


ft.app(target=main)
