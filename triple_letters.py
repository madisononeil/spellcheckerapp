from spelling_mistake import SpellingMistake as Sp

class TripleLettersinWord(Sp):
 
    def __init__(self, word):
        super().__init__(word)

    def get_tripleletters(self):

            triple_letters = set()

            for char in self.word:
                if char * 3 in self.word:
                    new_word = self.word.replace(char*3, char *2)
                    triple_letters.add(new_word)
        
            for char in self.word:
                if char * 3 in self.word:
                    new_word = self.word.replace(char*3, char)
                    triple_letters.add(new_word)

            return triple_letters
        