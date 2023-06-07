import os
import fnmatch


def find_file_by_mask(folder_path, file_pattern):
    try:
        files_and_dirs = os.listdir(folder_path)
        for file_or_dir in files_and_dirs:
            if fnmatch.fnmatch(file_or_dir, file_pattern):
                print(file_or_dir)

            if os.path.isdir(folder_path + file_or_dir):
                find_file_by_mask(folder_path + file_or_dir, file_pattern)
    except OSError:
        print('Error')
        exit()


folder_path_input = input('Введите директорию: ')
file_pattern_input = input('Введите маску файла: ')

find_file_by_mask(folder_path_input, file_pattern_input)
