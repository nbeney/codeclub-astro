from guizero import *
from resources import path_for
from logic import compare_words, COLOR_CORRECT, COLOR_MISPLACED, COLOR_WRONG
import random

IMAGE_ALPHABET = path_for("alphabet.png")
WORD_LIST_FILE = path_for("word-list.txt")
NUM_LETTERS = 5
NUM_GUESSES = 6


def load_word_list():
    """Load the word list from the file and return it as a list of words."""

    with open(WORD_LIST_FILE) as f:
        words = f.read().upper().splitlines()
        print(f"Loaded {len(words)} words")
        return words


def check_guess():
    colors = compare_words(guess, word)
    for idx, color in enumerate(colors):
        array[(idx, current_row)].bg = color
        if color == COLOR_WRONG:
            keyboard[guess[idx]].bg = "darkgrey"


def on_press_letter(ch):
    global guess, current_col

    if game_over or current_col >= NUM_LETTERS:
        return

    array[(current_col, current_row)].text = ch
    current_col += 1
    guess += ch


def on_press_enter():
    global guess, current_col, current_row, game_over

    if game_over or current_col < NUM_LETTERS:
        return

    check_guess()
    if guess == word:
        message.value = "You win!"
        message.text_color = "green"
        game_over = True
    elif current_row == NUM_GUESSES - 1:
        message.value = f"You lose! The word was {word}."
        message.text_color = "red"
        game_over = True
    else:
        current_col = 0
        current_row += 1
        guess = ""


def on_press_back():
    global guess, current_col

    if game_over:
        return

    if current_col > 0:
        current_col -= 1
        guess = guess[:-1]
        array[(current_col, current_row)].text = ""


def on_key(event):
    ch = event.key.upper()
    if ch in keyboard:
        on_press_letter(ch)
    elif event.keycode == 13:  # Enter
        on_press_enter()
    elif event.keycode == 8:  # Backspace
        on_press_back()


def make_key(master, text, grid, command, args=[], width=2):
    keyboard[text] = PushButton(
        master, text=text, width=width, grid=grid, command=command, args=args)
    keyboard[text].text_size = 15


if __name__ == "__main__":
    word_list = load_word_list()
    word = random.choice(word_list)
    array = {}
    keyboard = {}
    current_col = 0
    current_row = 0
    guess = ""
    game_over = False

    app = App(title="Wordle", width=600, height=810)

    Text(app)  # spacer

    # Make the title.
    box_title = Box(app)
    Picture(box_title, align="left", image=IMAGE_ALPHABET)
    Text(box_title, align="left", text="  Wordle  ", size=30)
    Picture(box_title, align="left", image=IMAGE_ALPHABET)

    Text(app)  # spacer

    # Make the array of guesses.
    box_grid = Box(app, layout="grid")
    for row in range(NUM_GUESSES):
        for col in range(NUM_LETTERS):
            letter = PushButton(box_grid, text="", grid=[col, row], width=3)
            letter.bg = "white"
            letter.text_size = 15
            letter.disable()
            array[(col, row)] = letter

    Text(app)  # spacer

    # Make the first row of the keyboard.
    box1 = Box(app, layout="grid")
    for idx, ch in enumerate("QWERTYUIOP"):
        make_key(box1, ch, grid=[idx, 0], command=on_press_letter, args=[ch])

    # Make the second row of the keyboard.
    box2 = Box(app, layout="grid")
    for idx, ch in enumerate("ASDFGHJKL"):
        make_key(box2, ch, grid=[idx, 0], command=on_press_letter, args=[ch])

    # Make the third row of the keyboard.
    box3 = Box(app, layout="grid")
    make_key(box3, "Enter", grid=[0, 0], command=on_press_enter, width=5)
    for idx, ch in enumerate("ZXCVBNM"):
        make_key(box3, ch, grid=[idx+1, 0], command=on_press_letter, args=[ch])
    make_key(box3, "Back", grid=[8, 0], command=on_press_back, width=5)

    Text(app)  # spacer

    message = Text(app, text="")
    message.text_size = 15

    app.when_key_released = on_key

    app.display()
