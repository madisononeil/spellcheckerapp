class DoubleLettersinWord:
    
    def __init__(self, word):
        if type(word) is not str:
            raise ValueError('Must enter a string value')
        self.word = word

    def get_doubleletters(self):
        double_letters= set()

        for char in self.word:
            new_word = self.word.replace(char, char *2)
            double_letters.add(new_word)

        for char in self.word:
            if char *2 in self.word:
                new_word = self.word.replace(char *2, char)
                double_letters.add(new_word)
        
        return double_letters


        
