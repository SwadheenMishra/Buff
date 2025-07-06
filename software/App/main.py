import flet as ft
import Challenge 
import camera

def main(page: ft.Page) -> None:
    page.title = "Wall-e"
    page.appbar = ft.AppBar(title=ft.Text("wall-e"), center_title=True, bgcolor="#4C7F86")
    page.bgcolor = "#223032"
    page.window.full_screen = True

    # Inputs
    goal_input = ft.TextField(
        label="Push-up Goal",
        width=200,
        border_radius=10,
        bgcolor="#1B2729",
        border_color="white",
        input_filter=ft.InputFilter(allow=True, regex_string=r"\d*")
    )

    timer_input = ft.TextField(
        label="Time (sec)",
        width=200,
        border_radius=10,
        bgcolor="#1B2729",
        border_color="white",
        input_filter=ft.InputFilter(allow=True, regex_string=r"\d*")
    )

    def on_start_click(e):
        check_and_start()

    start_btn = ft.ElevatedButton(
        text="Start Challenge",
        bgcolor="#4C7F86",
        color="white",
        on_click=on_start_click
    )

    def check_and_start():
        goal = goal_input.value.strip()
        timer = timer_input.value.strip()
        if goal and timer:
            try:
                goal = int(goal)
                timer = int(timer)
                Challenge.Start_challenge(page, goal, timer)
            except ValueError:
                Sbar = ft.SnackBar(ft.Text("⚠️ Goal and Timer must be numbers."))
                page.open(Sbar)
                page.update()
        else:
            Sbar = ft.SnackBar(ft.Text("⚠️ Upload an image and fill both fields."))
            page.open(Sbar)
            page.update()

    # Upload card
    challenge_card = ft.Card(
        elevation=6,
        content=ft.Container(
            on_click=camera.capture,
            width=900,
            height=500,
            bgcolor="#1B2729",
            alignment=ft.alignment.center,
            border_radius=10,
            content=ft.Column(
                controls=[
                    ft.Icon(ft.Icons.CAMERA_ALT, size=160, color="white"),
                    ft.Text("Click a Photo!", scale=1.5),
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            )
        )
    )

    # Layout
    page.add(
        ft.Column(
            controls=[
                ft.Row([goal_input, timer_input], alignment=ft.MainAxisAlignment.CENTER, spacing=30),
                ft.Container(height=10),
                ft.Row([start_btn], alignment=ft.MainAxisAlignment.CENTER),
                ft.Container(height=30),
                ft.Row([challenge_card], alignment=ft.MainAxisAlignment.CENTER),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )

if __name__ == "__main__":
    ft.app(target=main)