from guizero import *
from resources import path_for
from morse import text_to_morse, morse_to_text
import time

IMAGE_LOGO = path_for("logo.png")
IMAGE_SOUND = path_for("sound.png")

try:
    import winsound
    has_sound = True
except ModuleNotFoundError:
    has_sound = False


def on_change_text():
    text = textbox_text.value
    textbox_morse.value = text_to_morse(text)


def on_change_morse():
    morse = textbox_morse.value
    textbox_text.value = morse_to_text(morse)


def play_sound():
    morse = textbox_morse.value

    unit = 200
    dit_duration = unit
    dah_duration = unit * 3

    element_spacing = unit / 1000.0
    character_spacing = unit * 3 / 1000.0
    word_spacing = unit * 7 / 1000.0

    def beep(duration):
        freq = 800
        button_play.bg = "yellow"
        app.update()
        winsound.Beep(freq, duration)
        button_play.bg = None
        app.update()

    for ch in morse:
        if ch == '.':
            beep(dit_duration)
            time.sleep(element_spacing)
        elif ch == '-':
            beep(dah_duration)
            time.sleep(element_spacing)
        elif ch == ' ':
            time.sleep(character_spacing)
        else:
            time.sleep(word_spacing)


if __name__ == "__main__":
    app = App(title="Morse Code", width=500, height=560)

    Text(app)  # spacer

    Picture(app, image=IMAGE_LOGO)

    Text(app)  # spacer

    Text(app, text="Text", size=18)

    textbox_text = TextBox(
        app, multiline=True, width="fill", height=5, command=on_change_text
    )
    textbox_text.value = "HELLO WORLD!"

    Text(app)  # spacer

    Text(app, text="Morse", size=18)

    textbox_morse = TextBox(
        app, multiline=True, width="fill", height=5, command=on_change_morse
    )

    Text(app)  # spacer

    button_play = PushButton(
        app, image=IMAGE_SOUND, command=play_sound, enabled=has_sound
    )

    on_change_text()

    app.display()
