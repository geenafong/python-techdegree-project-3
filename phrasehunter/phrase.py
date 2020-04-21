from .character import Character


class Phrase(Character):
    def __init__(self, phrase):
        self.char_in_phrase = [] 
        letters_list = list(phrase)
        for char in letters_list:
            self.char_in_phrase.append(Character(char)) 

    def letters_in_phrase(self):
        phrase_letter_list = []
        for char in self.char_in_phrase:
            phrase_letter_list.append(char.show_original_character())
        return phrase_letter_list

    def guess_check(self, letter):
        for char in self.char_in_phrase:
            if char.correct_guess(letter):
                was_guessed = True
            else:
                was_guessed = False
        return was_guessed
    
    def guessed_all_letters(self):
        win_game = False
        if "_" not in self.letters_in_phrase():
            win_game = True
        return win_game
        
    
    
        
    
