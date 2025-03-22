import flet as ft 
 
def main(page:ft.Page):
    #page.theme= "dark"
    def handle_click(e):
        page.add(ft.Text("Clica aqui"))
        #page.update()
        
    ola = ft.Text("Se tá ligado!",size= 60, color ="blue", bgcolor = "yellow")
    botao = ft.ElevatedButton(text ="clica aqui",on_click = handle_click)

    page.add(ola,botao)
ft.app(target=main)
