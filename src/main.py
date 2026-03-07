import flet as ft
import os
import datetime
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
            self.df = pd.DataFrame(columns=['name','amount','paid','date'])
            self.df.to_csv(CSV_FILE, index=False)

        self.total_text = ft.Text(
            f"{self.df.loc[self.df["paid"] == False, "amount"].sum()}",
            size=40,
            weight=ft.FontWeight.BOLD,
            color="white"
        )
        self.debt_list = ft.Column(
            spacing=12,
            scroll=ft.ScrollMode.HIDDEN,
            expand=True
        )

        self.add_btn = ft.Button(
            "Add Debt",
            icon=ft.Icons.ADD_ROUNDED,
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.GREEN_700,
                padding=20,
                shape=ft.RoundedRectangleBorder(radius=12)
            ),
            on_click=self.open_add_debt,
            expand=True
        )
        self.pay_btn = ft.Button(
            "Pay Debt",
            icon=ft.Icons.PAYMENT,
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.BLUE_GREY_800,
                padding=20,
                shape=ft.RoundedRectangleBorder(radius=12)
            ),
            on_click=self.open_pay_debt,
            expand=True
        )
        
        
        self.ui_update()

    def build_ui(self):
        return ft.Container(
            padding=10,
            expand=True,
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Container(
                        ft.Column([
                            ft.Text("TOTAL UNPAID", size=12, color=ft.Colors.WHITE_70,weight="bold"),
                            ft.Row([
                                ft.Text("₦", size=24, color=ft.Colors.WHITE, weight="bold"),
                                self.total_text
                            ], vertical_alignment=ft.CrossAxisAlignment.START
                            ),
                        ], spacing=0
                        ),
                        bgcolor=ft.Colors.GREEN_800,
                        padding=15,
                        border_radius=20,
                        margin=ft.Margin.only(bottom=10)
                    ),
                    ft.Row([self.add_btn,self.pay_btn], spacing=15),
                    ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
                    ft.Row([
                        ft.Text("Recent Records", size=18, weight="bold"),
                        ft.Icon(ft.Icons.HISTORY, size=18),
                    ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Container(
                        expand=True,
                        content=self.debt_list
                    )
                ]
            )  
        )
        

    def open_add_debt(self):
        self.add_name = ft.TextField(label="Name",border_radius=10)  
        self.add_amount = ft.TextField(label="Amount",keyboard_type=ft.KeyboardType.NUMBER, border_radius=10)

        dialog = ft.AlertDialog(
            title="Add Debt",
            content=ft.Column([self.add_name,self.add_amount],spacing=15, height=140),
            actions=[
                ft.TextButton('Cancel', on_click=lambda e: self.page.pop_dialog()),
                ft.Button('Ok', bgcolor=ft.Colors.GREEN_700, color="white",on_click=self.add_debt)
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
            border_radius=10,
            options=[ft.dropdown.Option(name) for name in unpaid['name'].tolist()]
        )
        self.pay_amount = ft.TextField(label='Amount', keyboard_type=ft.KeyboardType.NUMBER,border_radius=10)

        dialog = ft.AlertDialog(
            title='Settle Debt',
            content=ft.Column([self.pay_name, self.pay_amount],height=140,spacing=15),
            actions=[
                ft.TextButton('Cancel', on_click= lambda e: self.page.pop_dialog()),
                ft.Button('pay',bgcolor=ft.Colors.GREEN_700, color="white", on_click=self.pay_debt)
            ],modal=True
        )
        self.page.show_dialog(dialog)

    def add_debt(self, e):
        name = self.add_name.value.strip()
        amount = self.add_amount.value.strip()

        if name and amount.isdigit():
            amount = int(amount)
            existing = self.df[(self.df["name"] == name) & (self.df["paid"] == False)]
            if not existing.empty:
                idx = existing.index[0]
                self.df.at[idx, "amount"] += amount
            else:
                new_row = pd.DataFrame([{
                    'name': name,
                    'amount': int(amount),
                    'paid': False,
                    'date': datetime.date.today().strftime("%B %d-%y")
                }])

                self.df = pd.concat([self.df, new_row], ignore_index=True)
            self.df.to_csv(CSV_FILE, index=False)

        self.page.pop_dialog()
        self.ui_update()

    def pay_debt(self, e):
        selected_name = self.pay_name.value
        amount = self.pay_amount.value.strip()
        if selected_name and amount.isdigit():
            ndex = self.df[(self.df["name"] == selected_name) & (self.df["paid"] == False)].index[0]
            self.df.at[ndex, "amount"] -= int(amount)
            if self.df.at[ndex, "amount"] <= 0:
                self.df.at[ndex, "amount"] = 0
                self.df.at[ndex, "paid"] = True
            self.df.to_csv(CSV_FILE, index=False)
        self.page.pop_dialog()
        self.ui_update()

    def ui_update(self):
        self.debt_list.controls.clear()
        for _, d in self.df.iloc[::-1].iterrows():
            is_paid = d["paid"]
            self.debt_list.controls.append(
                ft.Container(
                    bgcolor=ft.Colors.WHITE,
                    padding=15,
                    border=ft.Border.all(1, ft.Colors.BLUE_GREY_100),
                    border_radius=12,
                    content=ft.Row([
                        ft.Row([
                            ft.Icon(
                                ft.Icons.CHECK_CIRCLE if is_paid else ft.Icons.PENDING_OUTLINED,
                                color=ft.Colors.GREEN if is_paid else ft.Colors.ORANGE_700
                            ),
                            ft.Column([
                                ft.Text(d['name'],size=20, weight=ft.FontWeight.BOLD),
                                ft.Text("Paid" if is_paid else "Active", size=12, color="grey")
                            ],spacing=0)
                        ]),
                        ft.Column([
                            ft.Text(f"₦{d['amount']}",size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_700 if is_paid else ft.Colors.RED_400),
                            ft.Text(d['date']),
                            
                        ],spacing=2)
                        
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                        
                )
            )
        total = self.df.loc[self.df["paid"] == False, "amount"].sum()
        self.total_text.value = f"{total}"
        self.page.update()


def main(page: ft.Page):
    page.title = "Debt Tracker"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 400
    page.window.height = 700
    #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#F5F7F8"

    page.appbar = ft.AppBar(
        title=ft.Text("Debt Tracker", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_GREY_800),
        center_title=False, 
        
        bgcolor=ft.Colors.WHITE,
        elevation=0.5,
        actions=[
            ft.IconButton(
                icon=ft.Icons.SETTINGS_ROUNDED,
                icon_color=ft.Colors.BLUE_GREY_400,
                on_click=lambda _: print("Settings Clicked") # You can add a function here later
            ),
        ],
    )

    my_app = MyApp(page)
    page.update()   
    page.add(my_app.build_ui())

if __name__=="__main__":
    ft.run(main)
            