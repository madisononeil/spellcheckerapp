from transpose import TransposeOfWord
from double_letters import DoubleLettersinWord
from triple_letters import TripleLettersinWord

word = 'frog'
word1= 'appple'
word2 = 'moonkey'

extra_words = TransposeOfWord(word)
print(extra_words.get_transposes())

more_words = DoubleLettersinWord(word2)
print(more_words.get_doubleletters())

words_3 = TripleLettersinWord(word1)
print(words_3.get_tripleletters())