from spelling_mistake import SpellingMistake as Sp

class ProperNounMistakes(Sp):
    """inheritance class of SpellingMistake class that replaces the first letter of a word with a capital level and vise versa

    Args:
        Sp (str): word
    """

    def __init__(self, word):
        """creates word variable

        Args:
            word (str): misspelled word
        """
        super().__init__(word)

    def get_proper_capitalization(self):
        """takes a word and replaces first letter with capital letter or replaces with lowercase

        Returns:
            set : returns sets of all word possibilities
        """

        #creates empty set for word possibilities
        proper_capitalization = set()

        #checks if word is uppercase and makes it lower
        for i in range(65,91):
            if chr(i) == self.word[0]:
                new_word = self.word[0].lower() + self.word[1:]
                proper_capitalization.add(new_word)
        
        #checks if word is lowercase and makes it upper
        for i in range(97,123):
            if chr(i) == self.word[0]:
                new_word = self.word[0].upper() + self.word[1:]
                proper_capitalization.add(new_word)

        return proper_capitalization 


