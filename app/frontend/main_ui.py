import flet as ft

COLOR =ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["green","blue","green",],
            ) 

def main_ui():

    wel=ft.Column(
        controls=[
            ft.Text(value="Welcome",size=25,weight="bold"),
            ft.Text(value=".       to",size=20,weight="bold"),
            ft.Text(value="Debt Tracker",size=20,weight="bold")
        ]
    )
    return ft.Column(
        controls=[
            wel,
            ft.Row([
                ft.Container(
                    height=160,gradient=COLOR,
                    border_radius=7,width=170
                ),
                ft.Column([
                    ft.Container(
                    height=75,gradient=COLOR,
                    border_radius=7,width=170,
                    padding=ft.padding.only(bottom=0),
                ),
                ft.Container(
                    height=75,gradient=COLOR,
                    border_radius=7,width=170,
                    padding=ft.padding.only(bottom=0)

                )
                ])
            ]),
            ft.Container(
                height=80,gradient=COLOR,
                border_radius=10,
            ),
            ft.Text(value="Recent debt",size=15,weight="bold",),
            
            ft.Container(
                height=80,gradient=COLOR,
                border_radius=10,
            ),
            ft.Text(value="Recent debt",size=15,weight="bold",),
            
        ]
    )
