from guizero import *
from resources import path_for
import datetime
import inflect
import pyttsx3

IMAGE_LOUDSPEAKER = path_for("loudspeaker.png")


def on_update_clock():
    hour, minute, second = get_current_time()

    display_digit(hour // 10, 0, "blue", "lightblue")
    display_digit(hour % 10, 1, "blue", "lightblue")

    display_digit(minute // 10, 2, "green", "pale green")

    display_digit(minute % 10, 3, "green", "pale green")
    display_digit(second // 10, 4, "red", "pink")
    display_digit(second % 10, 5, "red", "pink")

    text_digits.value = f"{hour:02d}:{minute:02d}:{second:02d}"

    text_words.value = f"It is {time_to_words(hour, minute)}"


def on_click_loudspeaker():
    try:
        pyttsx3.speak(text_words.value)
    except Exception as ex:
        app.error("Error", f"An error occurred:\n{ex}")


def get_current_time():
    current_time = datetime.datetime.now()

    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    return (hour, minute, second)


def time_to_words(hour, minute):
    p = inflect_engine
    hour_words = p.number_to_words(hour)
    if minute == 0:
        minute_words = "o'clock"
    elif minute < 10:
        minute_words = "o'" + p.number_to_words(minute)
    else:
        minute_words = p.number_to_words(minute)
    return f"{hour_words} {minute_words}"


def display_digit(digit, x_pos, color_on, color_off):
    waffle_clock[x_pos, 3].color = color_on if digit & 1 else color_off
    waffle_clock[x_pos, 2].color = color_on if digit & 2 else color_off
    waffle_clock[x_pos, 1].color = color_on if digit & 4 else color_off
    waffle_clock[x_pos, 0].color = color_on if digit & 8 else color_off


if __name__ == "__main__":
    inflect_engine = inflect.engine()

    app = App(title="Binary Clock", width=250, height=300)

    Text(app, text="")  # spacer

    waffle_clock = Waffle(app, height=4, width=6, dotty=True)

    Text(app, text="")  # spacer

    text_digits = Text(app)

    # Text(app, text="")  # spacer

    text_words = Text(app)

    Text(app, text="")  # spacer

    button_loudspeaker = PushButton(
        app, image=IMAGE_LOUDSPEAKER, command=on_click_loudspeaker)

    on_update_clock()

    app.repeat(1000, on_update_clock)  # every 1000ms = 1sec

    app.display()
