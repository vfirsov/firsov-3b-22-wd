def read_file(file_name):
    try:
        file = open(file_name, 'r')
        return file.read()
    except OSError:
        print("Could not open/read file:")
        exit()


dictionary_counter = {}
words = read_file('text_with_words.txt')
words_arr = words.split()

for word in words_arr:
    word_in_lower_case = word.lower().replace(',', ' ').replace('.', ' ').strip()

    if word_in_lower_case in dictionary_counter:
        dictionary_counter[word_in_lower_case] += 1
    else:
        dictionary_counter[word_in_lower_case] = 1

for k, v in dictionary_counter.items():
    print(k, v)

