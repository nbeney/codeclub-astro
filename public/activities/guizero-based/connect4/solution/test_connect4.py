import connect4 as c4

E = c4.COLOR_EMPTY
O = c4.COLOR_ONE
T = c4.COLOR_TWO


def test_restart_sets_the_turn():
    game = c4.Game()
    game.restart()
    assert game.turn == c4.COLOR_ONE
    game.move(0)
    assert game.turn == c4.COLOR_TWO
    game.restart()
    assert game.turn == c4.COLOR_ONE


def test_restart_resets_the_grid():
    before = [[O, T, O], [O, T, O], [O, T, O]]
    after = [[E, E, E], [E, E, E], [E, E, E]]

    game = c4.Game(test_grid=before)
    assert game.grid == before
    game.restart()
    assert game.grid == after


def test_restart_calls_when_pixel_changed():
    before = [[O, T, O], [O, T, O], [O, T, O]]

    count = 0

    def callback(x, y, color):
        nonlocal count
        count += 1
        assert color == E

    game = c4.Game(test_grid=before, when_pixel_changed=callback)
    assert game.grid == before
    game.restart()
    assert count == 9


def test_restart_calls_when_turn_changed():
    before = [[O, T, O], [O, T, O], [O, T, O]]

    count = 0

    def callback(color):
        nonlocal count
        count += 1
        assert color == O

    game = c4.Game(test_grid=before, when_turn_changed=callback)
    assert game.grid == before
    game.restart()
    assert count == 1


def test_move_toggles_the_turn():
    game = c4.Game()
    game.restart()
    assert game.turn == c4.COLOR_ONE
    game.move(0)
    assert game.turn == c4.COLOR_TWO
    game.move(0)
    assert game.turn == c4.COLOR_ONE
    game.move(0)
    assert game.turn == c4.COLOR_TWO


def test_move_updates_the_grid():
    game = c4.Game(num_cols=2, num_rows=3)
    game.restart()
    assert game.grid == [[E, E, E], [E, E, E]]
    game.move(0)
    assert game.grid == [[E, E, O], [E, E, E]]
    game.move(0)
    assert game.grid == [[E, T, O], [E, E, E]]
    game.move(0)
    assert game.grid == [[O, T, O], [E, E, E]]


def test_move_calls_when_pixel_changed():
    count = 0

    def callback(x, y, color):
        nonlocal count
        count += 1
        if count <= 6:
            assert color == E
        elif count == 7:
            assert color == O
        elif count == 8:
            assert color == T
        elif count == 9:
            assert color == O

    game = c4.Game(num_cols=2, num_rows=3, when_pixel_changed=callback)
    game.restart()
    game.move(0)
    game.move(0)
    game.move(0)
    assert count == 9


def test_move_calls_when_turn_changed():
    count = 0

    def callback(color):
        nonlocal count
        count += 1
        if count == 1:
            assert color == O
        elif count == 2:
            assert color == T
        elif count == 3:
            assert color == O
        elif count == 4:
            assert color == T

    game = c4.Game(when_turn_changed=callback)
    game.restart()
    game.move(0)
    game.move(0)
    game.move(0)
    assert count == 4


def test_move_calls_when_invalid_move():
    before = [[O, T, O], [O, T, O], [O, T, O]]

    count = 0

    def callback():
        nonlocal count
        count += 1

    game = c4.Game(test_grid=before, when_invalid_move=callback)
    assert game.grid == before
    game.move(0)
    assert count == 1
    game.move(1)
    assert count == 2
    game.move(2)
    assert count == 3


def test_move_calls_when_game_over_with_win():
    before = [[E, O, T], [O, T, O], [O, T, T]]

    count = 0

    def callback(outcome):
        nonlocal count
        count += 1
        assert outcome == f"{O} wins!"

    game = c4.Game(test_grid=before, num_tokens=3, when_game_over=callback)
    game.move(0)
    assert count == 1


def test_move_calls_when_game_over_with_draw():
    before = [[E, O, T], [T, O, O], [O, T, T]]

    count = 0

    def callback(outcome):
        nonlocal count
        count += 1
        assert outcome == f"It's a draw..."

    game = c4.Game(test_grid=before, num_tokens=3, when_game_over=callback)
    game.move(0)
    assert count == 1


def test_is_valid_move():
    before = [[E, E, E], [E, E, O], [E, T, T], [O, T, T]]
    game = c4.Game(test_grid=before)
    assert game.is_valid_move(0) == True
    assert game.is_valid_move(1) == True
    assert game.is_valid_move(2) == True
    assert game.is_valid_move(3) == False


def test_valid_moves():
    before = [[E, E, E], [E, E, O], [E, T, T], [O, T, T]]
    game = c4.Game(test_grid=before)
    assert game.valid_moves() == [0, 1, 2]


def test_is_game_over_not_yet():
    before = [[E, O, T], [T, O, O], [O, T, T]]
    game = c4.Game(test_grid=before, num_tokens=3)
    assert game.is_game_over() == False


def test_is_game_over_with_draw():
    before = [[O, O, T], [T, O, O], [O, T, T]]
    game = c4.Game(test_grid=before, num_tokens=3)
    assert game.is_game_over() == "It's a draw..."


def test_is_game_over_with_win_horizontal():
    before = [[O, T, T], [O, O, O], [O, T, T]]
    game = c4.Game(test_grid=before, num_tokens=3)
    assert game.is_game_over() == f"{O} wins!"


def test_is_game_over_with_win_vertical():
    before = [[O, T, T], [T, O, O], [T, T, T]]
    game = c4.Game(test_grid=before, num_tokens=3)
    assert game.is_game_over() == f"{T} wins!"


def test_is_game_over_with_win_diag_up():
    before = [[E, E, O], [E, O, T], [O, T, T]]
    game = c4.Game(test_grid=before, num_tokens=3)
    assert game.is_game_over() == f"{O} wins!"


def test_is_game_over_with_win_diag_down():
    before = [[T, O, O], [E, T, O], [E, E, T]]
    game = c4.Game(test_grid=before, num_tokens=3)
    assert game.is_game_over() == f"{T} wins!"


# Attempt to run the pytest tests from IDLE (which does not have a built-in test runner like Visual Code or PyCharm do).
# Ideally we would simply call pytest.main(...) here, but it does not work from IDLE... :-(
# So instead we run pytest as a subprocess and print its output.
if __name__ == "__main__":
    import sys
    import subprocess

    cmd = [sys.executable, "-m", "pytest", sys.argv[0], "--verbose"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    print(result.stdout)
