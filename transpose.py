class TransposeOfWord:

    def __init__(self, word):
            self.word = word


    def get_transposes(self):
        transposes = set()
        split_word = [char for char in self.word]
        for i in range(len(split_word)-1):
            split_word[i], split_word[i+1] = split_word[i+1], split_word[i]
            new_word = ''.join(split_word)
            transposes.add(new_word)
            split_word[i+1], split_word[i] = split_word[i], split_word[i+1]
        return transposes


