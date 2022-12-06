class SpellingMistake:
    """base class for all spelling classes 
    """

    def __init__(self, word):
        """initializes a word variable and checks if it is a string

        Args:
            word (string): misspelled word

        Raises:
            ValueError: raises error if value is not a string
        """
        if type(word) is not str:
            raise ValueError('Must enter a string value')
        else:
            self.word = word
