class Dictionary:

    def __init__(self, file_name):
        self.file_name = file_name

    def words_in_dictionary(self):
        with open(self.file_name, 'r') as f:
            dictionary = [word.rstrip() for word in f]
            all_words= set(dictionary)
        return all_words

