class Character():
    def __init__(self, char, was_guessed=False):
        self.char = char
        self.was_guessed = was_guessed
    
    def correct_guess(self, guess):
        if guess == self.char:
            self.was_guessed = True

    def show_original_character(self):
        if self.was_guessed:
            return self.char
        elif self.char == ' ':
            return ' '
        else:
            return '_'