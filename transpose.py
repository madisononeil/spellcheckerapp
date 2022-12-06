from spelling_mistake import SpellingMistake as Sp

class TransposeOfWord(Sp):
    """inheritance class of SpellingMistake class that finds the individual transposes of two letters in word

    Args:
        Sp (str): word
    """

    def __init__(self, word):
        """creates word variable

        Args:
            word (str): misspelled word
        """
        super().__init__(word)

    def get_transposes(self):
        """finds all single letter transposes of word 

        Returns:
            set : returns set of all word possibilities
        """

        #creates empty set for word possibilities
        transposes = set()

        #split word into list
        split_word = [char for char in self.word]

        for i in range(len(split_word)-1):
            
            #switch letters and add word to set
            split_word[i], split_word[i+1] = split_word[i+1], split_word[i]
            new_word = ''.join(split_word)
            transposes.add(new_word)

            #switches letters back to go back into loop
            split_word[i+1], split_word[i] = split_word[i], split_word[i+1]

        return transposes


