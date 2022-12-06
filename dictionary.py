class Dictionary:
    """makes a dictionary of real words using dictionary text
    """

    def __init__(self, file_name):
        """gets a dictionary final

        Args:
            file_name (file): dictionary text file
        """
        self.file_name = file_name

    def words_in_dictionary(self):
        """opens the dictionary file and makes a set of all words in the file

        Returns:
            set: returns a set of dictionary words
        """
        #opens and reads dictionary file 
        with open(self.file_name, 'r') as f:
            dictionary = [word.rstrip() for word in f]
            all_words= set(dictionary)
        return all_words

