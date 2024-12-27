from guizero import *
from resources import path_for

IMAGE_LOGO = path_for("thermometer.png")


# Callback function for when the Celsius text changes.
def on_change_celsius():
    try:
        # CC:>>>>>
        celsius = float(textbox_celsius.value)
        textbox_farenheit.value = celsius_to_farenheit(celsius)
        # CC:<<<<<
        textbox_celsius.bg = "white"
        textbox_farenheit.bg = "white"
    except ValueError:
        textbox_farenheit.value = ""
        textbox_celsius.bg = "pink"
        textbox_farenheit.bg = "pink"


# Callback function for when the Farenheit text changes.
def on_change_farenheit():
    try:
        # CC:>>>>>
        farenheit = float(textbox_farenheit.value)
        textbox_celsius.value = farenheit_to_celsius(farenheit)
        # CC:<<<<<
        textbox_celsius.bg = "white"
        textbox_farenheit.bg = "white"
    except ValueError:
        textbox_celsius.value = ""
        textbox_celsius.bg = "pink"
        textbox_farenheit.bg = "pink"


# Function to convert from Celsius to Farenheit.
def celsius_to_farenheit(celsius):
    # CC:>>>>>
    return (celsius * 9 / 5) + 32
    # CC:<<<<<<


# Function to convert from Farenheit to Celsius.
def farenheit_to_celsius(farenheit):
    # CC:>>>>>
    return (farenheit - 32) * 5 / 9
    # CC:<<<<<


if __name__ == "__main__":
    app = App(title="Temperature Converter", width=400, height=300)

    Text(app, align="right", width=3)  # spacer

    Picture(app, align="right", image=IMAGE_LOGO)

    box_temperatures = Box(app, align="right", width="fill")

    Text(box_temperatures, text="Celsius", size=18)
    textbox_celsius = TextBox(
        box_temperatures, width=10, command=on_change_celsius)
    textbox_celsius.text_size = 18

    Text(box_temperatures)  # spacer

    Text(box_temperatures, text="Farenheit", size=18)
    textbox_farenheit = TextBox(
        box_temperatures, width=10, command=on_change_farenheit)
    textbox_farenheit.text_size = 18

    app.display()
