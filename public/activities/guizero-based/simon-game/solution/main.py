from guizero import *
from resources import path_for
from music import play_note
import random

IMAGE_LOGO = path_for("logo.png")

MUSIC_NOTES = ["G3", "C4", "E4", "G4"]
BRIGHT_COLORS = ["red", "green", "yellow", "blue"]
DIMMED_COLORS = ["#800000", "#006400", "#808000", "#000080"]

full_sequence = []
left_sequence = []
score = 0


def change_sequence(mode):
    global full_sequence, left_sequence, score

    match mode:
        case "reset":
            full_sequence = []
            score = 0
        case "start":
            full_sequence = [random.choice(box.children)]
            message.value = "Watch and memorize"
            score = 0
        case "expand":
            full_sequence.append(random.choice(box.children))
            message.value = "Watch and memorize"
            score += 1
        case _:
            raise ValueError(f"Invalid mode: {mode!r}")

    left_sequence = list(full_sequence)  # shallow copy
    play_many(full_sequence)

    if full_sequence:
        message.value = "Repeat"


def play_many(sequence):
    for button in sequence:
        play_one(button)


def play_one(button):
    button.bg = button.color_on
    app.update()
    play_note(button.music_note, 500)
    button.bg = button.color_off
    app.update()


def on_click(button):
    global left_sequence

    play_one(button)

    if left_sequence:
        if button == left_sequence[0]:
            left_sequence.pop(0)
            if not left_sequence:
                message.value = "Well done!"
                app.after(500, lambda: change_sequence("expand"))
        else:
            message.value = f"Game over - Score is {score} - Press Space to restart"
            change_sequence("reset")


def on_key(event):
    if event.key == " ":  # space
        change_sequence("start")


if __name__ == "__main__":
    app = App(title="Simon Game", width=500, height=650)

    Text(app)  # spacer

    Picture(app, image=IMAGE_LOGO)

    Text(app)  # spacer

    box = Box(app, layout="grid")
    PushButton(box, grid=[0, 0], text="", width=24, height=12)  # top left
    PushButton(box, grid=[1, 0], text="", width=24, height=12)  # top right
    PushButton(box, grid=[0, 1], text="", width=24, height=12)  # bottom left
    PushButton(box, grid=[1, 1], text="", width=24, height=12)  # bottom right

    for idx, button in enumerate(box.children):
        button.music_note = MUSIC_NOTES[idx]
        button.color_on = BRIGHT_COLORS[idx]
        button.color_off = DIMMED_COLORS[idx]
        button.bg = DIMMED_COLORS[idx]
        button.update_command(on_click, [button])

    Text(app)  # spacer

    message = Text(app, text="Press Space to start")

    app.when_key_released = on_key

    app.display()
