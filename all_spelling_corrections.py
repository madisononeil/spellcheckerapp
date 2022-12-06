"""module that uses as the different spelling classes to create all the possible spelling corrections 
"""
from transpose import TransposeOfWord
from double_letters import DoubleLettersinWord
from triple_letters import TripleLettersinWord
from single_letter_mistakes import SingleLetterMistakeofWord
from proper_noun_error import ProperNounMistakes
from adjacent_letter_mistake import AdjacentLetterMistake
from dictionary import Dictionary


#creates list of real dictionary words to compare to
word_list = Dictionary('dictionary.txt')
dictionary_words = word_list.words_in_dictionary()
 

def get_all_possibilities(word):
    """takes data from all Spelling classes and creates set of all
        possible real and non real word combinations 

    Args:
        word (str): misspelled word

    Returns:
        set: all possible spelling corrections of a given word
    """

    #calls all of the spelling classes
    transposes = TransposeOfWord(word)
    double_let = DoubleLettersinWord(word)
    triple_let = TripleLettersinWord(word)
    single_let= SingleLetterMistakeofWord(word)
    proper_noun= ProperNounMistakes(word)
    adjacent_let = AdjacentLetterMistake(word)

    #creates the set of all possibilties of words 
    all_possibilities_1 = transposes.get_transposes() | double_let.get_doubleletters() | triple_let.get_tripleletters() | \
        single_let.get_single_letter_mistake() | proper_noun.get_proper_capitalization() | adjacent_let.get_adjacent_letter_mistake()
    
    return all_possibilities_1  

def get_all_possibilities_2(word):
    """takes a given word and calls the get_all_possibilities function twice in order to use two spelling functions
        on the same word

    Args:
        word (string): misspelled word

    Returns:
        set: returns all the possible spelling corrections in a word based on dictionary list
    """

    #passes all the words through the get_all_possible mistake function and all the results through the function again
    all_possibilities_2 = [all_words for first_possiblitities in get_all_possibilities(word) for all_words in get_all_possibilities(first_possiblitities)]
    
    #checks if word is in dictionary and adds it to set of real world possibilities
    real_word_possibilities = set()
    for word in all_possibilities_2:
        if word in dictionary_words:
            real_word_possibilities.add(word)     
        
    return real_word_possibilities


