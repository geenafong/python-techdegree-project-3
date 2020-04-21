from phrasehunter.game import Game

phrase_list = ["chicken or egg", " dog eat dog", "cold turkey", "dark horse", "night owl", "big fish", "white elephant", "lone wolf"]

if __name__ == '__main__':
    game = Game(phrase_list)
    game.start_game()