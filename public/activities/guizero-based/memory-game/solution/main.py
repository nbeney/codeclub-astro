from guizero import *
from resources import path_for, find_images_in_dir
import random
import sys

NUM_COLS = 10
NUM_ROWS = 6

IMAGE_LOGO = path_for("logo.png")
IMAGE_BACK = path_for("question.png")
IMAGE_BLANK = path_for("blank.png")
DIR = path_for("animals")

WIDTH = 90
HEIGHT = 90

DELAY_MS = 1000

other_button = None


def set_image(button, image):
    button.image = image
    button.width = WIDTH
    button.height = HEIGHT


def on_restart():
    global other_button

    message.value = "Shuffling the cards..."
    app.update()

    other_button = None
    all_images = find_images_in_dir(DIR)

    if len(all_images) < NUM_COLS * NUM_ROWS // 2:
        app.error("Error", "Not enough images!")
        sys.exit()

    chosen_images = random.sample(all_images, NUM_COLS * NUM_ROWS // 2) * 2
    random.shuffle(chosen_images)

    for button in box.children:
        image = chosen_images.pop()
        button.image_path = image
        set_image(button, IMAGE_BACK)

    message.value = "Let's get started!"


def on_click(button):
    global other_button

    set_image(button, button.image_path)

    if other_button:
        if other_button.image_path == button.image_path:
            set_image(button, IMAGE_BLANK)
            set_image(other_button, IMAGE_BLANK)
        else:
            app.after(DELAY_MS, turn_back, [button])
            app.after(DELAY_MS, turn_back, [other_button])
        other_button = None
    else:
        other_button = button
        set_image(button, button.image_path)

    message.value = "Press Space to restart"


def on_key(event):
    if event.key == " ":  # space
        on_restart()


def turn_back(button):
    set_image(button, IMAGE_BACK)


if __name__ == "__main__":
    app = App(title="Memory", width=1000, height=800)

    Text(app, text="")  # spacer

    p = Picture(app, image=IMAGE_LOGO)

    Text(app, text="")  # spacer

    box = Box(app, layout="grid")

    for col in range(NUM_COLS):
        for row in range(NUM_ROWS):
            button = PushButton(box, grid=[col, row], text="")
            button.update_command(on_click, [button])

    Text(app, text="")  # spacer

    message = Text(app, text="")
    message.text_size = 20

    on_restart()

    app.when_key_released = on_key

    app.display()
