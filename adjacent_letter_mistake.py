from spelling_mistake import SpellingMistake as Sp

class AdjacentLetterMistake(Sp):

    def __init__(self, word):
        super().__init__(word)

    def get_adjacent_letter_mistake(self):

        adjacent_letter_mistake = set()

        group_1= 'qazwsx'
        group_2= 'saxdw'
        group_3= 'descf'
        group_4= 'fgtrv'
        group_5= 'gnbhty'
        group_6= 'hkyjun'
        group_7= 'mlkioj'
        group_8= 'pilok'

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
                        
