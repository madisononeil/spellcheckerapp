import string
from dictionary import Dictionary
import all_spelling_corrections as spellcheck


class SearchFile:
    """this class takes a file and reads it, and checks for misspelled words, gets correct spellings, fixes the spellings, 
        and returns a string of spelling suggestions

    Returns:
        str : returns a string of spelling suggestions for each individual misspelled words
    """

    #creates set of words using function from dictionary class
    word_list = Dictionary('dictionary.txt')
    dictionary_words = word_list.words_in_dictionary()

    def __init__(self, file_name):
        """initializes all variables in the class

        Args:
            file_name (.txt file): text file containing misspelled words
        """
        self.file_name = file_name

        #creates wordlists for all words in file and all misspelled words
        self.word_lst = []
        self.misspelled_wordlist = []
        #dictionary for misspelled word and their corrections
        self.correct_spellings = {}

    def get_file_information(self):
        """gets the file and adds all words to a word list
        """

        #empty list for words with no punct
        no_punct = ''
        
        #opens and read file
        with open(self.file_name, encoding='utf8') as f:
            my_file =f.read()
            for word in my_file:
                #adds words to list to strip all punctuation
                if word not in string.punctuation:
                    no_punct += word
            self.word_lst = no_punct.split()

    def get_misspelled_words(self):
        """checks words in file to dictionary set 

        Returns:
            list : returns list of all mispelled words in the file
        """

        for word in self.word_lst:
            #if word not in dictionary check the lowercase version of word
            if word not in SearchFile.dictionary_words:
                word = word.lower()
                #if word still not in dictionary add it to misspelled word list
                if word not in SearchFile.dictionary_words:
                    self.misspelled_wordlist.append(word)

        return self.misspelled_wordlist

    def get_correct_spellings(self):
        """for every misspelled word in file use a function in the spell check module to get possible spelling corrections

        Returns:
            dictionary : returns dictionary of mispelled word with spelling corrections
        """

        #call get_all_possibilities function for all misspelled words
        for word in self.misspelled_wordlist:
            self.correct_spellings[word] = spellcheck.get_all_possibilities_2(word)

        return self.correct_spellings

    def fix_spelling_corrections(self, misspelled_word, correct_word):
        """fixes spelling mistakes in textfile

        Args:
            misspelled_word (str): word that is misspelled
            correct_word (str): correct spelling of given misspelled word
        """

        #open and read the file, replace misspelled word with correct word
        with open(self.file_name, 'r', encoding='utf8') as f:
            my_file = f.read()
            my_file = my_file.replace(misspelled_word, correct_word)

        #fix the mistakes on the file
        with open(self.file_name, 'w', encoding='utf8') as f:
            f.write(my_file)

    def __str__(self):
        """edits the string function to give the user their spelling mistakes and corrections

        Returns:
            str : for each misspelled word print the word and its possible correct spelling
        """

        #creates empty string to add to
        corrections = ''

        #if their are no mistakes, print no spelling mistakes
        if self.misspelled_wordlist == []:
            return 'There are no spelling mistakes'

        else:
            #print each word and its corrections
            for word in self.misspelled_wordlist:
                corrections += f'\nThe word "{word}" in the following file "{self.file_name}" is spelled incorrectly.\n'
                corrections += f'\nDid you mean one of the following words:\n'
                corrections += ', '.join(self.correct_spellings[word])
                corrections += '\n'
                corrections += '_'*70
        
        return corrections
