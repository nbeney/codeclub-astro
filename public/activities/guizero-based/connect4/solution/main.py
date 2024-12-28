import random
import guizero as gz
import connect4 as c4
from resources import path_for

IMAGE_LOGO = path_for("logo.png")

PLAYERS = ["Human", "Random"]


class HumanPlayer:
    def __init__(self, game):
        self.game = game
        self.type = "Human"

    def play(self):
        pass


class RandomPlayer:
    def __init__(self, game):
        self.game = game
        self.type = "Random"

    def play(self):
        def doit():
            x = random.choice(game.valid_moves())
            game.move(x)

        delay_ms = 2000 - 2 * (slider_speed.value * 100)
        app.after(delay_ms, doit)  # wait half a second


def on_click(x, y):
    game.move(x)


def on_key(event):
    # Ignore special keys like Escape, Shift, etc.
    if not event.key:
        return

    # Convert the key to a column number (0-based).
    x = ord(event.key) - ord("1")

    if x in range(game.num_cols) and not game.is_game_over():  # is it a valid column number?
        on_click(x, 0)
    elif event.key == " ":  # is it a space?
        if game.is_game_over():
            ok = True
        else:
            ok = app.yesno("Restart", "Are you sure you want to restart?")

        if ok:
            game.restart()


def on_change_pixel(x, y, color):
    waffle[x, y].color = color


def on_change_turn(color):
    message.value = f"It is {color}'s turn."
    if color == c4.COLOR_ONE:
        player_one.play()
    else:
        player_two.play()


def on_invalid_move():
    app.info("Info", "Invalid move, try again.")


def on_game_over(outcome):
    message.value = f"Game over - {outcome} - press Space to restart"


def on_change_player_one(value):
    global player_one
    if value == "Human":
        player_one = HumanPlayer(game)
    else:
        player_one = RandomPlayer(game)
    game.restart()


def on_change_player_two(value):
    global player_two
    if value == "Human":
        player_two = HumanPlayer(game)
    else:
        player_two = RandomPlayer(game)
    game.restart()


if __name__ == "__main__":
    game = c4.Game(
        when_pixel_changed=on_change_pixel,
        when_turn_changed=on_change_turn,
        when_invalid_move=on_invalid_move,
        when_game_over=on_game_over,
    )

    player_one = RandomPlayer(game)
    player_two = RandomPlayer(game)

    app = gz.App(title="Connect Four", width=450, height=580)

    gz.Picture(app, image=IMAGE_LOGO, width=300, height=75)

    gz.Text(app, text="")  # spacer

    box_players = gz.Box(app)

    combo_player_one = gz.Combo(
        box_players, align="left", options=PLAYERS, command=on_change_player_one)
    combo_player_one.value = player_one.type
    combo_player_one.bg = game.color_one
    combo_player_one.text_color = "white"

    gz.Text(box_players, align="left", text="  vs  ")

    combo_player_two = gz.Combo(
        box_players, align="left", options=PLAYERS, command=on_change_player_two)
    combo_player_two.value = player_two.type
    combo_player_two.bg = game.color_two
    combo_player_two.text_color = "black"
    gz.Text(box_players, align="left", text="  Speed")
    slider_speed = gz.Slider(box_players, align="left", start=1, end=10)
    slider_speed.value = 5

    gz.Text(app, text="")  # spacer

    box_grid = gz.Box(app, border=1)
    box_grid.bg = "#555555"  # dark grey

    waffle = gz.Waffle(
        box_grid,
        width=game.num_cols,
        height=game.num_rows,
        dotty=True,
        dim=50,
        command=on_click,
    )

    gz.Text(app, text="")  # spacer

    message = gz.Text(app, text="")

    app.when_key_released = on_key

    game.restart()

    app.display()
