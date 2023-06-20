import os

FILES = {}


def find_file_by_mask(folder_path):
    try:
        files_and_dirs = os.listdir(folder_path)

        for file_or_dir in files_and_dirs:
            if os.path.isdir(folder_path + file_or_dir):
                find_file_by_mask(folder_path + file_or_dir)
            else:
                if FILES.get(file_or_dir) is None:
                    FILES[file_or_dir] = []

                FILES[file_or_dir].append({
                    'size': os.path.getsize(folder_path + "/" + file_or_dir),
                    'path': folder_path + file_or_dir
                })

    except OSError:
        print('Error')
        exit()


folder_path_input = input('Введите директорию: ')

find_file_by_mask(folder_path_input)
print(FILES)
