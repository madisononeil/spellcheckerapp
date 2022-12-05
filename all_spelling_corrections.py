from transpose import TransposeOfWord
from double_letters import DoubleLettersinWord
from triple_letters import TripleLettersinWord
from single_letter_mistakes import SingleLetterMistakeofWord
from proper_noun_error import ProperNounMistakes
from adjacent_letter_mistake import AdjacentLetterMistake
from dictionary import Dictionary

class AllSpellingCorrections:

    def __init__(self, word):
        self.word = word

    def get_all_possibilities(self):

        transposes = TransposeOfWord(self.word)
        double_let = DoubleLettersinWord(self.word)
        triple_let = TripleLettersinWord(self.word)
        single_let= SingleLetterMistakeofWord(self.word)
        proper_noun= ProperNounMistakes(self.word)
        adjacent_let = AdjacentLetterMistake(self.word)
        
        all_possibilities = transposes.get_transposes() | double_let.get_doubleletters() | triple_let.get_tripleletters() | \
            single_let.get_single_letter_mistake() | proper_noun.get_proper_capitalization() | adjacent_let.get_adjacent_letter_mistake()

        return all_possibilities

