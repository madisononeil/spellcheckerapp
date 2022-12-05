class Dictionary:

    def __init__(self) -> None:
        pass

    def words_in_dictionary(file_name):
        with open(file_name, 'r') as f:
            dictionary = [word.rstrip() for word in f]
            all_words= set(dictionary)
        return all_words

