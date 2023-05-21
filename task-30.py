string = input('строка')
vowels_list = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
vowels_count = 0
consonants_list = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
consonants_count = 0

for i in string:
    if i in vowels_list:
        vowels_count += 1

    if i in consonants_list:
        consonants_count += 1

print('гласных:', vowels_count)
print('согласных:', consonants_count)
