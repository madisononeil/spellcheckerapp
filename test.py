from transpose import TransposeOfWord
from double_letters import DoubleLettersinWord
from triple_letters import TripleLettersinWord
from single_letter_mistakes import SingleLetterMistakeofWord

word1 = 'frog'
word2 = 'moonkey'
word3= 'appple'
word4= 'me'
print(chr(98))

words_1 = TransposeOfWord(word1)
print(words_1.get_transposes())

words_2 = DoubleLettersinWord(word2)
print(words_2.get_doubleletters())

words_3 = TripleLettersinWord(word3)
print(words_3.get_tripleletters())

words_4= SingleLetterMistakeofWord(word4)
print(words_4.get_single_letter_mistake())