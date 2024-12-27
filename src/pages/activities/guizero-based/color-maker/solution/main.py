from guizero import *
from resources import path_for

IMAGE_PALETTE = path_for("palette.png")
IMAGE_WHEEL = path_for("color-wheel.png")


def mix_colors():
    # Get the amount of red, green, and blue from the sliders.
    r = red_slider.value
    g = green_slider.value
    b = blue_slider.value

    # Colors can be represented as a tuple of three integers (0-255).
    color_tuple = (r, g, b)

    # Colors can also be represented as a hex string.
    r_hex = f"{r:02X}"  # the amount of red in hexadecimal
    g_hex = f"{g:02X}"  # the amount of green in hexadecimal
    b_hex = f"{b:02X}"  # the amount of blue in hexadecimal
    color_hex = f"#{r_hex}{g_hex}{b_hex}"

    # Update the text to show the color values.
    patch_text.value = f"R = {r} = {r_hex}\nG = {g} = {g_hex}\nB = {b} = {b_hex}\n\n{color_hex}\n\n{color_tuple}"
    patch_text.bg = color_tuple  # or color_hex

    # Adjust the color of the text to improve readability.
    avg = (r + g + b) / 3
    patch_text.text_color = "white" if avg < 100 else "black"


def on_change_red(slider_value):
    # CC:>>>>>
    r = int(slider_value)
    red_slider.bg = (r, 0, 0)
    red_slider.text_color = "white" if r < 180 else "black"
    mix_colors()
    # CC:<<<<<


def on_change_green(slider_value):
    # CC:>>>>>
    g = int(slider_value)
    green_slider.bg = (0, g, 0)
    green_slider.text_color = "white" if g < 180 else "black"
    mix_colors()
    # CC:<<<<<


def on_change_blue(slider_value):
    # CC:>>>>>
    b = int(slider_value)
    blue_slider.bg = (0, 0, b)
    blue_slider.text_color = "white"
    mix_colors()
    # CC:<<<<<


def on_random():
    from random import randint
    red_slider.value = randint(0, 255)
    green_slider.value = randint(0, 255)
    blue_slider.value = randint(0, 255)


if __name__ == "__main__":
    app = App(title="Color Maker", width=500, height=500)

    Text(app)  # spacer

    box = Box(app)
    Picture(box, align="left", image=IMAGE_WHEEL)
    Text(box, align="left", text="  Color Maker  ", size=30)
    Picture(box, align="left", image=IMAGE_PALETTE)

    Text(app)  # spacer

    red_slider = Slider(app, start=0, end=255, width=400, command=on_change_red)
    red_slider.value = 144

    green_slider = Slider(app, start=0, end=255, width=400, command=on_change_green)
    green_slider.value = 126

    blue_slider = Slider(app, start=0, end=255, width=400, command=on_change_blue)
    blue_slider.value = 255

    Text(app)  # spacer

    PushButton(app, text="Random", command=on_random)

    Text(app)  # spacer

    patch_text = Text(app, size=16, width="fill", height="fill")

    app.display()
