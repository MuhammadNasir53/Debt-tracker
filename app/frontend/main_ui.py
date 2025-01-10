import flet as ft


def main(page: ft.page):
    page.window.width = 380
    page.window.heiht = 480

    _maim = ft.Column(
        controls=[
            
        ]
    )

    page.add()
    page.update()

if __name__=="__main__":
    ft.app(target=main)    