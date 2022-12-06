from spelling_mistake import SpellingMistake as Sp

class TripleLettersinWord(Sp):
    """inheritance class of SpellingMistake class that replaces the triple letters 
        in the word with double letters and with single letters

    Args:
        Sp (str): word
    """
 
    def __init__(self, word):
        """creates word variable

        Args:
            word (str): misspelled word
        """
        super().__init__(word)

    def get_tripleletters(self):
        """replaces the triple letters in the word with double letters and with single letters


        Returns:
            set: returns sets of all word possibilities
        """

        #creates an empty set for all possible word combos
        triple_letters = set()

        #replaces triple letters with double letters
        for char in self.word:
            if char * 3 in self.word:
                new_word = self.word.replace(char*3, char *2)
                triple_letters.add(new_word)

        #replaces triple letters with single letters
        for char in self.word:
            if char * 3 in self.word:
                new_word = self.word.replace(char*3, char)
                triple_letters.add(new_word)

        return triple_letters
        