from game import Game


game = Game()

def play_game():
    
    game.greet_user()
    while True:
        game.draw_state()
        game.get_input()
        if game.win_ch is not None:
            break



if __name__ == '__main__':
    play_game()