from spelling_mistake import SpellingMistake as Sp

class DoubleLettersinWord(Sp):
    """inheritance class of SpellingMistake class that replaces the letters 
        in the word with double letters and replaces it with single letters and 
        vise versa

    Args:
        Sp (str): word
    """
    
    def __init__(self, word):
        """creates word variable

        Args:
            word (str): misspelled word
        """
        super().__init__(word)

    def get_doubleletters(self):
        """gets the letters in the word with double letters 
        and replaces it with single letters and vise versa

        Returns:
            set: returns sets of all word possibilities
        """

        #empty set for word possibilities
        double_letters= set()

        #if word has single letter make it double letter
        for char in self.word:
            new_word = self.word.replace(char, char *2)
            double_letters.add(new_word)

        #if word has double letter make it single letter
        for char in self.word:
            if char *2 in self.word:
                new_word = self.word.replace(char *2, char)
                double_letters.add(new_word)
        
        return double_letters


        
