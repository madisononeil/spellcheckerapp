from spelling_mistake import SpellingMistake as Sp

class AdjacentLetterMistake(Sp):
    """inheritance class of SpellingMistake class that replaces the letters 
        in the word with letters adjacent to it on the keyboard

    Args:
        Sp (str): word
    """

    def __init__(self, word):
        """creates word variable

        Args:
            word (str): misspelled word
        """
        super().__init__(word)

    def get_adjacent_letter_mistake(self):
        """replaces the letters in the word with letters 
            adjacent to it on the keyboard

        Returns:
            returns sets of all word possibilities
        """

        #creates empty set to put new words in
        adjacent_letter_mistake = set()

        #groups of adjacent keyboard keys
        group_1= 'qazwsx'
        group_2= 'saxdw'
        group_3= 'descf'
        group_4= 'fgtrv'
        group_5= 'gnbhty'
        group_6= 'hkyjun'
        group_7= 'mlkioj'
        group_8= 'pilok'

        #if the letter is in the word and the letter is in the group, 
        #it will replace letter with adjacent keyboard letters
        for char in self.word:
            for letter in group_1:
                if char == letter:
                    for letter in group_1:
                        new_word = self.word.replace(char, letter)
                        adjacent_letter_mistake.add(new_word)

        for char in self.word:
            for letter in group_2:
                if char == letter:
                    for letter in group_2:
                        new_word = self.word.replace(char, letter)
                        adjacent_letter_mistake.add(new_word)

        for char in self.word:
            for letter in group_3:
                if char == letter:
                    for letter in group_3:
                        new_word = self.word.replace(char, letter)
                        adjacent_letter_mistake.add(new_word)

        for char in self.word:
            for letter in group_4:
                if char == letter:
                    for letter in group_4:
                        new_word = self.word.replace(char, letter)
                        adjacent_letter_mistake.add(new_word)

        for char in self.word:
            for letter in group_5:
                if char == letter:
                    for letter in group_5:
                        new_word = self.word.replace(char, letter)
                        adjacent_letter_mistake.add(new_word)

        for char in self.word:
            for letter in group_6:
                if char == letter:
                    for letter in group_6:
                        new_word = self.word.replace(char, letter)
                        adjacent_letter_mistake.add(new_word)

        for char in self.word:
            for letter in group_7:
                if char == letter:
                    for letter in group_7:
                        new_word = self.word.replace(char, letter)
                        adjacent_letter_mistake.add(new_word)

        for char in self.word:
            for letter in group_8:
                if char == letter:
                    for letter in group_8:
                        new_word = self.word.replace(char, letter)
                        adjacent_letter_mistake.add(new_word)

        return adjacent_letter_mistake
                        
