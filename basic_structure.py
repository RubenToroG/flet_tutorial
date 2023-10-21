import flet as ft
import time

def main(page: ft.Page):
    #Controls
    t = ft.Text(value='Hello World', color='green')
    page.controls.append(t)
    page.update()

    #Modify control properties
    t = ft.Text()
    page.add(t) #It's a shortcut for page.controls.append(t) and the page.update()
    for i in range(2):
        t.value = f'Step {i}'
        page.update()
        time.sleep(0.5)

    #Some controls could contain other controls
    page.add(
        ft.Row(controls=[
            ft.Text('Control A'),
            ft.TextField(label='Your name'),
            ft.ElevatedButton(text='Say my name!! please')
        ])
    )

    #
    for i in range(2):
        page.controls.append(ft.Text(f'Line {i}'))
        if i > 4:
            page.controls.pop(0)
        page.update()
        time.sleep(0.3)

    #Some controls, could have event handlers reacting on a user input
    def button_clicked(e):
        page.add(ft.Text('Clicked'))
    page.add(ft.ElevatedButton(text='Click!!', on_click=button_clicked))

#Se puede especificar el puerto ft.app(port=8850, target...)
ft.app(target=main, view=ft.AppView.FLET_APP_WEB)