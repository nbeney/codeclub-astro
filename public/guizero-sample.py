# Import the widgets we need from the guizero library.
from guizero import App, Text, PushButton, Slider, Combo

# Callback function for when the button is clicked.
def on_click_button():
    global click_count
    click_count += 1
    message.value = f"You clicked {click_count} times"

# Callback function for when the slider is moved.
def on_move_slider(value):
    message.text_size = value

# Callback function for when the combo box is changed.
def on_change_combo(value):
    message.text_color = value
    combo.bg = value
    combo.text_color = "white" if value == "blue" else "black"

if __name__ == "__main__":
    # Initialize some variables.
    click_count = 0

    # Create the main window.
    app = App(title="Welcome to Guizero", width=400, height=200, bg="#b9f2ff")

    # Add some widgets to the main window.
    message = Text(app, text="You haven't clicked yet", color="red")
    button = PushButton(app, text="Click me!", command=on_click_button)
    slider = Slider(app, start=12, end=64, command=on_move_slider)
    combo = Combo(app, options=["red", "green", "blue"], command=on_change_combo)
    combo.bg = "red"

    # Start the event loop. This should be the last line of your program.
    app.display()
