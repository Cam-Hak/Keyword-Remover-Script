import re ; import os

file_name = r'keyword.txt'
os.system(' open keyword.txt')
enter_to_continue = input('Press ENTER to continue: ')
word_removal = input('Enter what should be removed: ')

string = open(file_name).read()
new_str = re.sub(word_removal, '', string)
open(file_name, 'w').write(new_str)

enter_to_continue2 = input('Press ENTER to load .txt file: ')
os.system('open keyword.txt')