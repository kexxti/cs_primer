from game import Game


game = Game()

def play_game():
    
    game.greet_user()
    game.draw_state()
    game.get_input()
    game.update_state()


if __name__ == '__main__':
    play_game()