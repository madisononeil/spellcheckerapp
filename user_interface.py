from search_file import SearchFile

print('_'*80)
print('\nHello, welcome to the spellchecker app!')

edit_more_files = True
while edit_more_files:

    print('_'*80)
    text_file =input('\nPlease enter a text file that needs spelling checked: ')
    print('_'*80)
    
    searching_file = SearchFile(text_file)
    searching_file.get_file_information()
    searching_file.get_misspelled_words()
    searching_file.get_correct_spellings()
    print(searching_file.__str__())
    
    if not searching_file.get_misspelled_words():

        continue_program = input('\nWould you like to correct another file(Y/N)?: ')
    
    else:
        continue_edit_text = input('\nWould you like to replace a word(Y/N)?: ')
        
        edit_text = True
        while edit_text:
            if continue_edit_text == 'Y':

                misspelling = input('\nWhich misspelled word would you like to replace?: ')
                correct_spelling = input('Which word would you like to replace it with?: ')
                
                searching_file.fix_spelling_corrections(misspelling, correct_spelling)
                print('_'*80)
                print('\nThe correction was made to the file.')
                print('_'*80)

                continue_edit_text = input('\nWould you like to replace another word(Y/N)?: ')
            
            if continue_edit_text == 'N':
                edit_text = False
    


    continue_program = input('\nWould you like to correct another file(Y/N)?: ')

    if continue_program == 'N':
        edit_more_files = False

print('_'*80)
print('Thank you for using my spellchecker app, goodbye!')
print('_'*80)