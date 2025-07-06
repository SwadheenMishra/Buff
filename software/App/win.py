import flet as ft

def win_screen(page: ft.Page) -> None:
    page.clean()
    page.title = "You win!"

    page.bgcolor = "#00DDFF"
    page.add(ft.Row(controls=[ft.Text("You Win!", scale=6, color=ft.Colors.BLACK87)], expand=True, alignment=ft.MainAxisAlignment.CENTER))
    page.update()

if __name__ == "__main__":
    ft.app(target=win_screen)