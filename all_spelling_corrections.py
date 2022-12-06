from transpose import TransposeOfWord
from double_letters import DoubleLettersinWord
from triple_letters import TripleLettersinWord
from single_letter_mistakes import SingleLetterMistakeofWord
from proper_noun_error import ProperNounMistakes
from adjacent_letter_mistake import AdjacentLetterMistake
from dictionary import Dictionary



word_list = Dictionary('dictionary.txt')
dictionary_words = word_list.words_in_dictionary()
 

def get_all_possibilities(word):

    transposes = TransposeOfWord(word)
    double_let = DoubleLettersinWord(word)
    triple_let = TripleLettersinWord(word)
    single_let= SingleLetterMistakeofWord(word)
    proper_noun= ProperNounMistakes(word)
    adjacent_let = AdjacentLetterMistake(word)

    all_possibilities_1 = transposes.get_transposes() | double_let.get_doubleletters() | triple_let.get_tripleletters() | \
        single_let.get_single_letter_mistake() | proper_noun.get_proper_capitalization() | adjacent_let.get_adjacent_letter_mistake()
    
    return all_possibilities_1  

def get_all_possibilities_2(word):


    all_possibilities_2 = [all_words for first_possiblitities in get_all_possibilities(word) for all_words in get_all_possibilities(first_possiblitities)]
    
    real_word_possibilities = set()
    for word in all_possibilities_2:
        if word in dictionary_words:
            real_word_possibilities.add(word)     
        
    return real_word_possibilities


