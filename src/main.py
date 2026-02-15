import flet as ft
import os
import pandas as pd

CSV_FILE = "debt.csv"

class MyApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.title = "Debt Tracker"
        # self.root = self.build_ui

        if os.path.exists(CSV_FILE):
            self.df = pd.read_csv(CSV_FILE)
        else:
            self.df = pd.DataFrame(columns=['name','amount','paid'])
            self.df.to_csv(CSV_FILE, index=False)

        self.total_text = ft.Text(
            f"Debt: {self.df.loc[self.df["paid"] == False, "amount"].sum()}",
            size=20,
            weight=ft.FontWeight.BOLD
        )
        self.debt_list = ft.Column(
            spacing=10,
            scroll=ft.ScrollMode.HIDDEN
        )

        self.add_btn = ft.FilledButton(
            content="Add Debt",
            height=40,
            expand=True,
            on_click=self.open_add_debt
        )
        self.pay_btn = ft.FilledButton(
            content="Pay Debt",
            height=50,
            expand=True,
            on_click=self.open_pay_debt
        )
        self.ui_update()

    def build_ui(self):
        return ft.Column(
            expand=True,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[ft.Text(self.title,size=22, weight=ft.FontWeight.BOLD),]
                ),
                ft.Container(
                    bgcolor='green',
                    height=70,
                    border_radius=22,
                    padding=22,
                    content=ft.Row([self.total_text],alignment=ft.MainAxisAlignment.START)
                ),
                ft.Row([self.add_btn,self.pay_btn], spacing=12),
                ft.Container(
                    expand=True,
                    content=self.debt_list
                )
            ]
        )  

    def open_add_debt(self):
        self.add_name = ft.TextField(label="Name")  
        self.add_amount = ft.TextField(label="Amount",keyboard_type=ft.KeyboardType.NUMBER)

        dialog = ft.AlertDialog(
            title="Add Debt",
            content=ft.Column([self.add_name,self.add_amount],spacing=20),
            actions=[
                ft.TextButton('Cancel', on_click=lambda e: self.page.pop_dialog()),
                ft.TextButton('Ok', on_click=self.add_debt)
            ],
            modal=True
        )
        self.page.show_dialog(dialog)

    def open_pay_debt(self):
        unpaid = self.df[self.df['paid'] == False]
        if unpaid.empty:
            dlg = ft.AlertDialog(
                title='Pay Debt',
                content=ft.Text('No debt to pay'),
                actions=[
                    ft.TextButton('Ok', on_click=lambda e: self.page.pop_dialog()),
                ],
                modal=True
            ) 
            self.page.show_dialog(dlg)
            return
        self.pay_name = ft.Dropdown(
            label='select name',
            enable_filter=True,
            options=[ft.dropdown.Option(name) for name in unpaid['name'].tolist()]
        )
        self.pay_amount = ft.TextField(label='Amount', keyboard_type=ft.KeyboardType.NUMBER)

        dialog = ft.AlertDialog(
            title='Pay Debt',
            content=ft.Column([self.pay_name, self.pay_amount]),
            actions=[
                ft.TextButton('Cancel', on_click= lambda e: self.page.pop_dialog())
            ],modal=True
        )
        self.page.show_dialog(dialog)

    def add_debt(self, e):
        name = self.add_name.value.strip()
        amount = self.add_amount.value.strip()

        if name and amount.isdigit():
            new_row = pd.DataFrame([{
                'name': name,
                'amount': int(amount),
                'paid': False
            }])

            self.df = pd.concat([self.df, new_row], ignore_index=True)
            self.df.to_csv(CSV_FILE, index=False)

        self.page.pop_dialog()
        self.ui_update()

    def ui_update(self):
        self.debt_list.controls.clear()
        for _, d in self.df.iloc[::-1].iterrows():
            self.debt_list.controls.append(
                ft.Container(
                    padding=10,
                    bgcolor="green",
                    border_radius=10,
                    content=ft.Row([
                        ft.Text(d['name'],size=22, weight=ft.FontWeight.BOLD),
                        ft.Text(d['amount'],size=22, weight=ft.FontWeight.BOLD)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                )
            )
        total = self.df.loc[self.df["paid"] == False, "amount"].sum()
        self.total_text.value = f"Debt: {total}"
        self.page.update()


def main(page: ft.Page):
    page.title = "Debt Tracker"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 450
    page.window.height = 600
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    my_app = MyApp(page)
    page.update()   
    page.add(my_app.build_ui())

if __name__=="__main__":
    ft.run(main)
            