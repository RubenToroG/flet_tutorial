import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(value='Hello, Calculator App'))

ft.app(target=main)