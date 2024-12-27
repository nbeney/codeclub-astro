NUM_COLS = 7
NUM_ROWS = 6
NUM_TOKENS = 4
COLOR_EMPTY = "white"
COLOR_ONE = "blue"
COLOR_TWO = "yellow"


class Game:
    def __init__(
        self,
        num_cols=NUM_COLS,
        num_rows=NUM_ROWS,
        num_tokens=NUM_TOKENS,  # the number of tokens to align to win
        color_empty=COLOR_EMPTY,
        color_one=COLOR_ONE,
        color_two=COLOR_TWO,
        when_pixel_changed=lambda x, y, color: None,
        when_turn_changed=lambda color: None,
        when_invalid_move=lambda: None,
        when_game_over=lambda outcome: None,
        test_grid=None,  # for unit testing only
    ):
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.num_tokens = num_tokens
        self.color_empty = color_empty
        self.color_one = color_one
        self.color_two = color_two
        self.when_pixel_changed = when_pixel_changed
        self.when_turn_changed = when_turn_changed
        self.when_invalid_move = when_invalid_move
        self.when_game_over = when_game_over

        if test_grid:
            self.num_cols = len(test_grid)
            self.num_rows = len(test_grid[0])
            self.grid = test_grid
            count_one = self.count_tokens(self.color_one)
            count_two = self.count_tokens(self.color_two)
            self.turn = self.color_two if count_one > count_two else self.color_one

    def restart(self):
        self.grid = [[self.color_empty] *
                     self.num_rows for _ in range(self.num_cols)]
        for x in range(self.num_cols):
            for y in range(self.num_rows):
                self.when_pixel_changed(x, y, self.grid[x][y])
        self.turn = self.color_one
        self.when_turn_changed(self.turn)

    def move(self, x):
        y = self.__find_next_y(x)
        if y is None:
            self.when_invalid_move()
        else:
            self.grid[x][y] = self.turn
            self.when_pixel_changed(x, y, self.grid[x][y])
            if outcome := self.is_game_over():
                self.when_game_over(outcome)
            else:
                self.__toggle_turn()

    def is_game_over(self):
        if winner := self.__find_winner():
            return f"{winner} wins!"

        for x in range(self.num_cols):
            if self.is_valid_move(x):
                return False

        return "It's a draw..."

    def is_valid_move(self, x):
        return self.grid[x][0] == self.color_empty

    def valid_moves(self):
        return [x for x in range(self.num_cols) if self.is_valid_move(x)]

    def __find_next_y(self, x):
        y = self.num_rows - 1  # bottom row
        while y >= 0:
            if self.grid[x][y] == self.color_empty:
                return y
            y -= 1  # move one row up
        return None

    def __toggle_turn(self):
        self.turn = self.color_two if self.turn == self.color_one else self.color_one
        self.when_turn_changed(self.turn)

    def __find_winner(self):
        for x in range(self.num_cols):
            for y in range(self.num_rows):
                if self.__check(x, y):
                    return self.grid[x][y]
        return None

    def __check(self, x, y):
        if self.grid[x][y] == self.color_empty:
            return False

        return (
            self.__check_horizontal(x, y)
            or self.__check_vertical(x, y)
            or self.__check_diagonal_up(x, y)
            or self.__check_diagonal_down(x, y)
        )

    def __check_horizontal(self, x, y):
        if x + self.num_tokens > self.num_cols:
            return False

        for i in range(1, self.num_tokens):
            if self.grid[x + i][y] != self.grid[x][y]:
                return False

        return True

    def __check_vertical(self, x, y):
        if y + self.num_tokens > self.num_rows:
            return False

        for i in range(1, self.num_tokens):
            if self.grid[x][y + i] != self.grid[x][y]:
                return False

        return True

    def __check_diagonal_up(self, x, y):
        if x + self.num_tokens > self.num_cols or y + self.num_tokens > self.num_rows:
            return False

        for i in range(1, self.num_tokens):
            if self.grid[x + i][y + i] != self.grid[x][y]:
                return False

        return True

    def __check_diagonal_down(self, x, y):
        if x + self.num_tokens > self.num_cols or y - self.num_tokens < -1:
            return False

        for i in range(1, self.num_tokens):
            if self.grid[x + i][y - i] != self.grid[x][y]:
                return False

        return True

    def count_tokens(self, color):
        count = 0
        for x in range(self.num_cols):
            for y in range(self.num_rows):
                if self.grid[x][y] == color:
                    count += 1
        return count
