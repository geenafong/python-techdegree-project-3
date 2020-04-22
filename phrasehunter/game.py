# Create your Game class logic in here.
import random
from .phrase import Phrase
from .character import Character


class Game():
    def __init__(self, phrases):
        self.phrases = phrases
        self.current = random.choice(phrases)
        self.lives = 5
    
    def reset(self):
        self.lives = 5
        self.current = random.choice(self.phrases)

    def play_again_win(self, win):  
        if win == True:
            play_again = str(input("You won! Want to play again? (y/n) "))
        if win == False:
            play_again = str(input("You lost. Want to play again? (y/n) "))
        if play_again == 'y':
            self.reset()
            self.start_game()
        else:
            print("Thanks for playing")
            exit()

    def welcome(self):
        print("-" * 30)
        print("Welcome to phrase hunter.")
        print("-" * 30)
        print("\nLet's see if you can guess the phrase that we have provided.")
        print("Hint: All words are a well known animal idiom.\n")

    def start_game(self):
        phrase = Phrase(self.current)
        self.welcome()
        correct_letters = str(set(self.current))
        while self.lives in range(0,6):
            try: 
                print(' '.join(phrase.letters_in_phrase()))
                guessed_letter = input("\nGuess a letter: ").lower()
                if guessed_letter.isalpha() and len(guessed_letter) == 1:
                    phrase.guess_check(str(guessed_letter))
                    if str(guessed_letter) not in correct_letters:
                        self.lives -= 1
                        print(f"Letter not in phrase. You have {self.lives} guess(es) left.\n")
                        if self.lives == 0:
                            self.play_again_win(win=False)
                    if phrase.guessed_all_letters():
                        self.play_again_win(win=True)
                else:
                    print("Please enter a single alphabetical character.")
            except ValueError:
                print("You must enter a letter a-z.")
