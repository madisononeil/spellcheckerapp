from spelling_mistake import SpellingMistake as Sp

class SingleLetterMistakeofWord(Sp):

    def __init__(self, word):
        super().__init__(word)
    
    def get_single_letter_mistake(self):

        single_letter_mistake = set()

        for char in self.word:
            for i in range(97, 123):
                new_word = self.word.replace(char, char + chr(i))
                single_letter_mistake.add(new_word)

        for char in self.word:
            for i in range(97, 123):
                new_word = self.word.replace(char, chr(i))
                single_letter_mistake.add(new_word)

        for char in self.word:
            word_new = self.word.replace(char, '')
            single_letter_mistake.add(word_new)

        return single_letter_mistake

