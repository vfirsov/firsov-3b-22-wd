import os

file_name = str(input('Введите имя файла '))

file_folder = './'
file_path = os.path.join(file_folder, file_name)


if os.path.isfile(file_path):
    try:
        file = open(file_path, 'r')
        print(file.read())
    except OSError:
        print("Could not open/read file:")
        exit()
else:
    print("file not exit:")
