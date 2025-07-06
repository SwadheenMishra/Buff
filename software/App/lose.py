import flet as ft
import InstaHelper

def lose_screen(page: ft.Page) -> None:
    page.clean()
    page.title = "You Lose!"

    page.bgcolor = "#FF0000"
    page.add(ft.Row(controls=[ft.Text("You Lose!\nNow the picture\nwill be uploaded on\ninstagram!!!", scale=5, color=ft.Colors.BLACK87)], expand=True, alignment=ft.MainAxisAlignment.CENTER))
    page.update()

    #InstaHelper.upload(f"img.jpg", "@codeday_lucknow This guy couldn't even do {goal} push ups LOLLL - WallE")

if __name__ == "__main__":
    ft.app(target=lose_screen)
