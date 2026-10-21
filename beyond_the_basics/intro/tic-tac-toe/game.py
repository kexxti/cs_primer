class Game:
    def __init__(self, game_state=None):
        self.game_state = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.win_states = [
            [[1, 0, 0], [1, 0, 0], [1, 0, 0]],
            [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
            [[0, 0, 1], [0, 0, 1], [0, 0, 1]],
            [[1, 1, 1], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [1, 1, 1], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [1, 1, 1]],
            [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            [[0, 0, 1], [0, 1, 0], [1, 0, 0]],
        ]
        self.win_ch = None

    def update_state(self, i, j, ch):
        try:
            self.game_state[i][j] = ch
            if self._is_end():
                self.game_over()
        except IndexError:
            print("Index error occured")

    def get_input(self):
        i, j, ch = input().split()
        self.update_state(int(i), int(j), ch)

    def greet_user(self):
        print("This is tic-tac-toe bruv")
        print("To make a turn -- type cell index")
        print("The the upper left cell has index (0,0)")
        print("Good luck!")
        print()

    # Если хотя бы одна маска подходит (маскированными остаются одинаковые символы -> игра окончена)
    def _is_end(self):
        for mask in self.win_states:
            masked_values = self._apply_mask(mask, self.game_state)
            if len(masked_values) == 1 and " " not in masked_values:
                self.win_ch = masked_values.pop()
                return True

        return False

    def draw_state(self):
        print(f"{'  -' * 7}\n")

        for i in range(3):
            for j in range(3):
                print(f"  |  {self.game_state[i][j]}", end="")

            print("  |  \n")
            print(f"{'  -' * 7}\n")

    def game_over(self):
        print(f"The game is over. The winner is {self.win_ch}")

    def _apply_mask(self, mask, state):
        masked_values = []
        for i in range(3):
            for j in range(3):
                if mask[i][j] == 1:
                    masked_values.append(state[i][j])

        return set(masked_values)
