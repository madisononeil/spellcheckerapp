from spelling_mistake import SpellingMistake as Sp

class SingleLetterMistakeofWord(Sp):
    """inheritance class of SpellingMistake class that replaces the letters 
        in the word with different letter, same letter and different letter, and deletes one letter

    Args:
        Sp (str): word
    """
    

    def __init__(self, word):
        """creates word variable

        Args:
            word (str): misspelled word
        """
        super().__init__(word)
    
    def get_single_letter_mistake(self):
        """finds all single letter different combos of a misspelled words

        Returns:
            set : returns set of all word possibilities
        """

        #creates empty set for word possibilities
        single_letter_mistake = set()

        #adds an extra letter between every letter in the word
        for char in self.word:
            for i in range(97, 123):
                new_word = self.word.replace(char, char + chr(i))
                single_letter_mistake.add(new_word)

        #replaces a letter for each letter in word
        for char in self.word:
            for i in range(97, 123):
                new_word = self.word.replace(char, chr(i))
                single_letter_mistake.add(new_word)

        #deletes a letter for each letter in word
        for char in self.word:
            word_new = self.word.replace(char, '')
            single_letter_mistake.add(word_new)

        return single_letter_mistake

