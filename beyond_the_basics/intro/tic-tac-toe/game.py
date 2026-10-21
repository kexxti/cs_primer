class Game:
    def __init__(self, game_state=None):
        game_state = [[], [], []]
        win_states = [
            [[1, 0, 0], [1, 0, 0], [1, 0, 0]],
            [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
            [[0, 0, 1], [0, 0, 1], [0, 0, 1]],
            [[1, 1, 1], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [1, 1, 1], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [1, 1, 1]],
            [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            [[0, 0, 1], [0, 1, 0], [1, 0, 0]],
        ]

    def update_state(self): ...

    def get_input(self): ...

    def greet_user(self):
        print("This is tic-tac-toe bruv")
        print("To make a turn -- type cell index")
        print("The the upper left cell has index (0,0)")
        print("Good luck!")
        print()

    def _is_end(self): ...
    
    def draw_state(self):
        print(f"{'-' * 25}\n")
        
        for i in range(3):
            for j in range(3):
                print(f"  |  {self.game_state[i][j]}")
                 
            print('  |  \n')
            
            print(f"{'-' * 25}\n")
        
        
        