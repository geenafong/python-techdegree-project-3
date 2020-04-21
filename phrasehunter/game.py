# Create your Game class logic in here.
import random
from .phrase import Phrase
from .character import Character

class Game():
    def __init__(self, phrases):
        self.phrases = phrases
        self.current = random.choice(phrases)
        
    
    def start_game(self):
        phrase = Phrase(self.current)
        print("\nWelcome to phrase hunter. \nLet's see if you can guess the phrase that we have provided.\n\n")
        print(self.current)
        correct_letters = str(set(self.current))
        number_of_incorrect_guesses = 0
        while number_of_incorrect_guesses<5:
            try:
                print(' '.join(phrase.letters_in_phrase()))
                guessed_letter = input("\nGuess a letter: ").lower()
                if guessed_letter.isalpha() == False or len(guessed_letter) > 1:
                    print("Please enter a single alphabetical character.")
                phrase.guess_check(str(guessed_letter))
                if str(guessed_letter) not in correct_letters:
                    number_of_incorrect_guesses += 1
                    print(f"Letter not in phrase. You have {number_of_incorrect_guesses} out of 5 guesses left.\n")
                    if number_of_incorrect_guesses == 5:
                        play_again = input("You lost. Want to play again? (y/n) ")
                        if play_again == 'y':
                            self.start_game()
                        elif play_again == 'n':
                            print("Thanks for playing")
                            break
                        else:
                            print("dont understand")
                if phrase.guessed_all_letters():
                    play_again = str(input("You win! Want to play again? (y/n) "))
                    if play_again == 'y':
                        self.start_game()
                    else:
                        print("Thanks for playing")
                        exit()
            except ValueError:
                print("Not a letter, please try again")