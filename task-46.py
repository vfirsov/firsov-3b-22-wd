import os

file_name = 'text.txt'
file_folder = './'
file_path = os.path.join(file_folder, file_name)


if os.path.isfile(file_path):
    try:
        text_txt = open("new_file.txt", "w")
        text_txt.write('Hello, world!')
    except OSError:
        print("Could not write file:")
        exit()
else:
    print("file not exit:")
