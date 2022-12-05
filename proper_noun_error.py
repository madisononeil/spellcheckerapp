from spelling_mistake import SpellingMistake as Sp

class ProperNounMistakes(Sp):

    def __init__(self, word):
        super().__init__(word)

    def get_proper_capitalization(self):

        proper_capitalization = set()

        for i in range(65,91):
            if chr(i) == self.word[0]:
                new_word = self.word[0].lower() + self.word[1:]
                proper_capitalization.add(new_word)

        for i in range(97,123):
            if chr(i) == self.word[0]:
                new_word = self.word[0].upper() + self.word[1:]
                proper_capitalization.add(new_word)

        return proper_capitalization 


