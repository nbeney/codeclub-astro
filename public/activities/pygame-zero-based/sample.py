# Import the whole pgzrun library.
import pgzrun

# Define the size of the window.
WIDTH = 400
HEIGHT = 300

# Initialize some variables.
text_angle = 0
text_pos = (WIDTH / 2, HEIGHT / 2)

# Callback function to redraw the screen.
def draw():
    screen.fill("forestgreen")
    screen.draw.text("Welcome to\nPygame Zero!", center=text_pos, fontsize=48, angle=text_angle, color="red", ocolor="white", owidth=2)

# Callback function to update the game. It is called at every frame.
def update():
    global text_angle
    text_angle -= 0.25

# Callback function to handle mouse clicks.
def on_mouse_down(pos, button):
    print("Mouse button", button, "clicked at", pos)
    global text_pos
    text_pos = pos

# Callback function to handle key presses.
def on_key_down(key, mod):
    print("Key down", key, "with mod", mod)
    global text_angle, text_pos
    if key == keys.SPACE:
        text_angle = 0
        text_pos = (WIDTH / 2, HEIGHT / 2)
    
# Start the event loop. This should be the last line of your program.
pgzrun.go()
