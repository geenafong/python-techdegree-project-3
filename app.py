from phrasehunter.game import Game

phrase_list = ["chicken or egg", " dog eat dog", "cold turkey", "dark horse", "night owl", "big fish", "white elephant", "lone wolf"]

if __name__ == '__main__':
    try:
        game = Game(phrase_list)
        game.start_game()
    except (ValueError, RuntimeError, TypeError, NameError):
        print("Game not able to execute.")