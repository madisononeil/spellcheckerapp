class SpellingMistake:

    def __init__(self, word):
        if type(word) is not str:
            raise ValueError('Must enter a string value')
        else:
            self.word = word
