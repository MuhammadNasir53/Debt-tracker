import asyncio
import flet as ft
from app.frontend.main_ui import main_ui  # Adjust the import path as per your project structure

async def show_first_view(page):
    # First view content
    page.views.clear()
    page.views.append(ft.View(
        controls=[
            ft.Text("This is the first view. It will change in 3 seconds."),
        ]
    ))
    page.update()
    # Wait for 3 seconds
    await asyncio.sleep(3)
    show_second_view(page)

def show_second_view(page):
    # Second view content
    page.views.clear()
    page.views.append(ft.View(
        controls=[
            main_ui()  # Show your custom UI from the imported module
        ]
    ))
    page.update()

def main(page: ft.Page):
    page.window.width = 380
    page.window.height = 840
    page.title = "Debt Tracker App"
    # Show the first view initially
    asyncio.run(show_first_view(page))

ft.app(target=main)
