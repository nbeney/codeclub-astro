from guizero import *
from resources import path_for, find_images_in_dir
from data import CAPITALS_BY_COUNTRY, CATEGORIES, COUNTRIES_BY_CAPITAL
import random
import string

DIR = path_for("hangman")

secret = ""
clicked = []
hangman_images = find_images_in_dir(DIR, extension=".jpg")
hangman_idx = 0


def format(text, clicked):
    result = []
    for letter in text.replace(" ", "  "):
        if letter not in string.ascii_uppercase or letter in clicked:
            result.append(letter)
        else:
            result.append("_")
    return " ".join(result)


def reset():
    global hangman_idx

    for button in box.children:
        button.bg = "lightgray"
        button.text_color = "black"
        button.enable()

    clicked.clear()
    display.value = format(secret, clicked)
    hangman_idx = 0
    hangman.image = hangman_images[hangman_idx]


def on_change_category():
    global secret

    reset()
    secret_orig = random.choice(CATEGORIES[category.value])
    secret = secret_orig.upper()
    clicked.clear()
    display.value = format(secret, clicked)

    if category.value == "Countries":
        hint = CAPITALS_BY_COUNTRY[secret_orig]
    else:
        hint = COUNTRIES_BY_CAPITAL[secret_orig]
    message.value = hint


def on_click(button):
    global hangman_idx

    letter = button.text
    if letter in clicked:
        return

    clicked.append(letter)
    button.disable()

    display.value = format(secret, clicked)

    if letter in secret:
        button.bg = "green"
        button.text_color = "white"
    else:
        button.bg = "yellow"
        hangman_idx += 1
        hangman.image = hangman_images[hangman_idx]


def on_key(event):
    key = event.key.upper()
    idx = string.ascii_uppercase.find(key)
    if idx >= 0 and idx < len(box.children):
        button = box.children[idx]
        on_click(button)
    elif event.keycode == 13:  # return
        on_change_category()


if __name__ == "__main__":
    app = App(title="Hangman Game", width=600, height=875)

    Text(app)  # spacer

    Text(app, text="HANGMAN", size=30, color="red")

    Text(app)  # spacer

    names = sorted(CATEGORIES.keys())
    category = Combo(app, options=names, command=on_change_category)

    Text(app)  # spacer

    hangman = Picture(app, image=hangman_images[hangman_idx])

    Text(app)  # spacer

    display = Text(app, size=20)

    Text(app)  # spacer

    box = Box(app, layout="grid")
    for idx, letter in enumerate(string.ascii_uppercase):
        x = idx % 9
        y = idx // 9
        button = PushButton(box, text=letter, grid=[x, y], width=2)
        button.text_size = 15
        button.update_command(on_click, [button])

    Text(app)  # spacer

    message = Text(app, text="...", size=20)

    on_change_category()

    app.when_key_released = on_key

    app.display()
