import flet as ft

def main(page: ft.Page) -> None:
    page.title = "Test"
    page.appbar = ft.AppBar(title=ft.Text("Push ups (idk)"), center_title=True, bgcolor="#4C7F86")
    page.bgcolor = "#223032"

    # Card with centered icon
    challenge_card = ft.Card(
        elevation=6,
        content=ft.Container(
            width=300,
            height=400,
            bgcolor="#1B2729",
            alignment=ft.alignment.center,
            border_radius=10,
            content=ft.Icon(ft.Icons.UPLOAD, size=80, color="white")
        )
    )

    # Center the card in the page
    page.add(
        ft.Column(
            controls=[challenge_card],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
