import string
from dictionary import Dictionary
import all_spelling_corrections as spellcheck


class SearchFile:

    word_list = Dictionary('dictionary.txt')
    dictionary_words = word_list.words_in_dictionary()

    def __init__(self, file_name):
        self.file_name = file_name
        self.word_lst = []
        self.misspelled_wordlist = []
        self.correct_spellings = {}

    def get_file_information(self):
        no_punct = ''

        with open(self.file_name, encoding='utf8') as f:
            my_file =f.read()
            for word in my_file:
                if word not in string.punctuation:
                    no_punct += word
            self.word_lst = no_punct.split()

    def get_misspelled_words(self):

        for word in self.word_lst:
            if word not in SearchFile.dictionary_words:
                word = word.lower()
                if word not in SearchFile.dictionary_words:
                    self.misspelled_wordlist.append(word)

        return self.misspelled_wordlist

    def get_correct_spellings(self):

        for word in self.misspelled_wordlist:
            self.correct_spellings[word] = spellcheck.get_all_possibilities_2(word)

        return self.correct_spellings

    def fix_spelling_corrections(self, misspelled_word, correct_word):
        with open(self.file_name, 'r', encoding='utf8') as f:
            my_file = f.read()
            my_file = my_file.replace(misspelled_word, correct_word)
        with open(self.file_name, 'w', encoding='utf8') as f:
            f.write(my_file)

    def __str__(self):

        corrections = ''

        if self.misspelled_wordlist == []:
            return 'There are no spelling mistakes'

        else:
            for word in self.misspelled_wordlist:
                corrections += f'\nThe word "{word}" in the following file "{self.file_name}" is spelled incorrectly.\n'
                corrections += f'\nDid you mean one of the following words:\n'
                corrections += ', '.join(self.correct_spellings[word])
                corrections += '\n'
                corrections += '_'*70
        
        return corrections
