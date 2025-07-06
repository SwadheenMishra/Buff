import flet as ft
import threading
import sensorData 
import time

def Start_challenge(page: ft.Page, goal: int, timeL: int):
    page.clean()
    page.title = "Push-up Counter"
    page.bgcolor = "#223032"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    value = 100
    pushup_goal = goal
    countdown = timeL  # seconds

    BAR_HEIGHT = 300
    ARROW_HEIGHT = 20
    value_clamped = max(0, min(100, value))
    arrow_offset = (100 - value_clamped) / 100 * (BAR_HEIGHT - ARROW_HEIGHT)

    # Arrow
    arrow = ft.Text("◀", size=25, color="red", weight=ft.FontWeight.BOLD)
    arrow_container = ft.Container(
        content=arrow,
        alignment=ft.alignment.top_center,
        height=ARROW_HEIGHT,
        width=30,
        bgcolor="transparent"
    )

    # Colored bar
    top_zone = ft.Container(height=BAR_HEIGHT * 0.25, bgcolor="green", width=20)
    mid_zone = ft.Container(height=BAR_HEIGHT * 0.5, bgcolor="yellow", width=20)
    bottom_zone = ft.Container(height=BAR_HEIGHT * 0.25, bgcolor="green", width=20)

    vertical_bar = ft.Column(controls=[top_zone, mid_zone, bottom_zone], spacing=0)
    bar_column = ft.Container(content=vertical_bar, width=20, height=BAR_HEIGHT, border_radius=10)

    arrow_column = ft.Container(
        content=arrow_container,
        width=30,
        height=BAR_HEIGHT,
        padding=ft.Padding(left=0, top=arrow_offset, right=0, bottom=0),
        bgcolor="transparent"
    )

    # Counter and timer text
    # Counter text
    counter_text = ft.Text(f"Pushups: 0 / {pushup_goal}", size=18, color="white")

    # Circular timer
    timer_label = ft.Text(f"{int(countdown)}s", size=16, color="white", weight=ft.FontWeight.BOLD)
    progress_ring = ft.ProgressRing(
        value=1.0,
        width=60,
        height=60,
        stroke_width=6,
        color="red",
        bgcolor="#333333"
    )

    timer_circle = ft.Stack([
        progress_ring,
        ft.Container(content=timer_label, alignment=ft.alignment.center, width=60, height=60)
    ])

    # Info column next to the bar
    info_column = ft.Column(
        controls=[counter_text, timer_circle],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )


    # Full horizontal layout
    layout = ft.Row(
        controls=[
            bar_column,
            arrow_column,
            ft.Container(width=30),  # spacing
            info_column
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(layout)

    # Push-up detection logic
    pushup_count = 0
    state = "up"
    threshold_down = 30
    threshold_up = 85

    def win():
        counter_text.value = "✅ You Win!"
        page.update()

    def lose():
        counter_text.value = "❌ Time's up!"
        page.update()

    def timer_thread():
        nonlocal countdown
        while countdown > 0:
            time.sleep(0.1)
            countdown -= 0.1
            countdown = round(countdown, 1)

            timer_label.value = f"{int(countdown)}s"
            progress_ring.value = countdown / 30  # Normalize to 1.0 max
            page.update()

    if pushup_count < pushup_goal:
        lose()


    threading.Thread(target=timer_thread, daemon=True).start()

    def showcase():
        nonlocal pushup_count, state

        while True:
            new_value = sensorData.get_distance()
            if new_value is not None:
                if new_value > 70:
                    new_value *= 3
                value_clamped = max(0, min(100, new_value))
                arrow_offset = (100 - value_clamped) / 100 * (BAR_HEIGHT - ARROW_HEIGHT)

                arrow_column.padding = ft.Padding(left=0, top=arrow_offset, right=0, bottom=0)
                arrow_column.update()

                if state == "up" and value_clamped < threshold_down:
                    state = "down"
                elif state == "down" and value_clamped > threshold_up:
                    state = "up"
                    pushup_count += 1
                    counter_text.value = f"Pushups: {pushup_count} / {pushup_goal}"
                    page.update()
                    if pushup_count >= pushup_goal:
                        win()
                        return


    threading.Thread(target=showcase, daemon=True).start()
