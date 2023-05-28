import os

file = 'text.txt'

if os.path.isfile(os.path.join('./', file)):
    text_txt = open(file, 'r')
    print(text_txt.read())
else:
    print('file not exist')
    exit()
