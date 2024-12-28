from guizero import *
from resources import path_for
import inflect
import pyttsx3
import random

IMAGE_LETTERS = path_for("letters.png")
IMAGE_VOICE = path_for("loudspeaker.png")


def on_click_number(number):
    # CC:>>>>>
    app.last_number = number
    update_table()
    # CC:<<<<<


def on_click_letters():
    # CC:>>>>>
    app.use_words = not app.use_words
    update_table()
    # CC:<<<<<


def on_click_loudspeaker():
    # CC:>>>>>
    text = text_table.value
    text = text.replace(" x ", " times ")
    text = text.replace(" = ", " is ")

    try:
        pyttsx3.speak(text)
    except Exception as ex:
        app.error("Error", f"An error occurred:\n{ex}")
    # CC:<<<<<


def update_table():
    # CC:>>>>>
    p = inflect_engine
    number = app.last_number
    table = []

    for n in range(1, 12 + 1):
        if app.use_words:
            table.append(
                f"{p.number_to_words(number)} x {p.number_to_words(n)} =  {p.number_to_words(number * n)}")
        else:
            table.append(f"{number} x {n} = {number * n}")

    text_table.value = "\n".join(table)
    # CC:<<<<<


if __name__ == "__main__":
    inflect_engine = inflect.engine()

    app = App(title="Times Tables", width=500, height=650)

    Text(app)  # spacer

    box = Box(app, layout="grid")
    PushButton(box, text="1", grid=[0, 0])
    PushButton(box, text="2", grid=[1, 0])
    PushButton(box, text="3", grid=[2, 0])
    PushButton(box, text="4", grid=[3, 0])
    PushButton(box, text="5", grid=[4, 0])
    PushButton(box, text="6", grid=[5, 0])
    PushButton(box, text="7", grid=[0, 1])
    PushButton(box, text="8", grid=[1, 1])
    PushButton(box, text="9", grid=[2, 1])
    PushButton(box, text="10", grid=[3, 1])
    PushButton(box, text="11", grid=[4, 1])
    PushButton(box, text="12", grid=[5, 1])

    COLORS = ["red", "orange", "yellow", "green", "blue", "purple",
              "pink", "brown", "black", "white", "gray", "cyan"]

    for idx, button in enumerate(box.children):
        button.width = 4
        button.height = 1
        button.text_size = 18
        button.bg = COLORS[idx]
        if COLORS[idx] in ["black", "blue", "purple", "brown", "gray"]:
            button.text_color = "white"
        button.update_command(on_click_number, [idx + 1])

    Text(app)  # spacer

    text_table = Text(app, size=18)

    Text(app)  # spacer

    tools = Box(app)

    PushButton(
        tools, align="left", image=IMAGE_LETTERS, command=on_click_letters
    )

    Text(tools, align="left", text="", width="5")  # spacer

    PushButton(
        tools, align="left", image=IMAGE_VOICE, command=on_click_loudspeaker
    )

    app.last_number = random.randint(1, 12)
    app.use_words = False

    update_table()

    app.display()
