import os

EXCLUDE = {
    'venv': True,
    '.git': True,
    '.idea': True
}


def object_assign(first, second):
    result = first.copy()

    for k in second:
        if result.get(k) is None:
            result[k] = second.get(k)
        elif hasattr(result, k) & hasattr(second, k):
            result[k] = result.get(k).extend(second.get(k))

    return result


def collect_files_to_map(folder_path):
    files = {}
    files_and_dirs = os.listdir(folder_path)

    for file_or_dir in files_and_dirs:

        if EXCLUDE.get(file_or_dir):
            continue

        path = folder_path + '/' + file_or_dir

        if os.path.isdir(path):
            files_in_folder = collect_files_to_map(path)
            files = object_assign(files, files_in_folder)
        else:
            size = os.path.getsize(path)

            if size != 0:
                key_of_file = file_or_dir + '_' + str(size)

                if files.get(key_of_file) is None:
                    files[key_of_file] = []

                files[key_of_file].append(path)

    return files


def remove_duplicates(files_map):
    for key in files_map:
        if len(files_map[key]) > 1:
            first = files_map[key][0]
            print('stay', first)

            for remove_file_index in range(1, len(files_map[key])):
                print('will remove', files_map[key][remove_file_index])


def remove_duplicate_files(folder_path):
    try:
        files_map = collect_files_to_map(folder_path)
        remove_duplicates(files_map)

    except OSError:
        print('Error')
        exit()


folder_path_input = input('Введите директорию: ')

remove_duplicate_files(folder_path_input)

