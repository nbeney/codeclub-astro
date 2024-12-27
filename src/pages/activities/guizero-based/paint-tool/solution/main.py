from guizero import *
from resources import path_for

IMAGE_UNDO = path_for("undo.png")
IMAGE_BIN = path_for("bin.png")


def on_left_button_pressed(event):
    global last_x, last_y

    history.append([])
    last_x = event.x
    last_y = event.y


def on_mouse_dragged(event):
    global last_x, last_y

    id = canvas.line(
        last_x, last_y, event.x, event.y, color=last_color, width=width.value)
    history[-1].append(id)

    if symmetry.value:
        id = canvas.line(
            canvas.width - last_x, last_y, canvas.width - event.x, event.y, color=last_color, width=width.value)
        history[-1].append(id)

    last_x = event.x
    last_y = event.y


def on_color_clicked(x, y):
    global last_color

    last_color = palette[x, y].color


def on_undo_clicked():
    if len(history) > 0:
        for id in history.pop():
            canvas.delete(id)


def on_bin_clicked():
    if len(history) > 0 and app.yesno("Clear", "Are you sure?"):
        canvas.clear()
        history.clear()


if __name__ == "__main__":
    history = []
    last_x = 0
    last_y = 0
    last_color = "red"

    app = App(title="Paint Tool", width=600, height=400)

    tools = Box(app, align="bottom")
    palette = Waffle(
        tools, align="left", width=7, height=1, dotty=True, command=on_color_clicked)
    palette[0, 0].color = "red"
    palette[1, 0].color = "green"
    palette[2, 0].color = "blue"
    palette[3, 0].color = "yellow"
    palette[4, 0].color = "white"
    palette[5, 0].color = "darkgrey"
    palette[6, 0].color = "black"
    Text(tools, align="left", text="  Width")
    width = Slider(tools, align="left", start=1, end=10)
    width.value = 5
    symmetry = CheckBox(tools, align="left", text="Symmetry")
    PushButton(tools, align="left", image=IMAGE_UNDO, command=on_undo_clicked)
    PushButton(tools, align="left", image=IMAGE_BIN, command=on_bin_clicked)

    canvas = Drawing(app, width=app.width, height=app.height)
    canvas.when_left_button_pressed = on_left_button_pressed
    canvas.when_mouse_dragged = on_mouse_dragged

    app.display()
