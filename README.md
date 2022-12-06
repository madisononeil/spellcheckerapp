# spellcheckerapp

The app that I developed is a spellchecker app. Therefore, the apps’ primary purpose is to check words in a text file to see if the words are spelled correctly and, if the word is spelled incorrectly, the app will also give suggestions to the user to help them decipher the correct spelling of the word. If a word in file is written as ‘smmile’, the app will tell the user they spelled the word incorrectly. The application will check the words in the file and compare these words to a dictionary list of words. Because the word is not in the dictionary, the app will look for all possible single transpositions of adjacent letters, double or triple letters, and incorrect single/double letter mistakes, and adjacent keyboard letters. The possible spelling suggestions will also be compared to the dictionary so the user will only be given valid English word suggestions. Then it will give spelling suggestions of real words like ‘smile’ to help the user find the correct spelling.
	
Another main feature of the app is giving the user the option to replace the misspelled word in the file with one of the app’s given spelling suggestions. The user will provide the misspelled word that they want to fix and provide the correctly spelled word that they want to replace the word with. The program will swap out the word in the file with the correct spelling given. The user has the option to correct one word, all the words, or none of the words. Once the user exits the program and checks their text file, they will see that the changes to the file have been made. 

The code has been broken up into 2 modules and 9 classes. The modules include a user interface and an all_spelling_corrections module. The user interface takes user input and calls the specific classes and functions based on user input. The all_spelling_corrections module uses all the spelling classes to obtain a set of all possible spelling corrections for the user. The 9 classes include a dictionary class, a search file class, a spelling base (or parent) class and 6 spelling subclasses. The dictionary class creates a dictionary so the misspelled words in the file a can be identified, and the spelling suggestions can be checked to ensure they are valid English words. The search file class takes a file and reads it, and checks for misspelled words, gets correct spellings, fixes the spellings, and returns a string of spelling suggestions. The 7 spelling classes derive the possible spelling corrections for a given misspelled word. 

