def count_letters(filename):
    letters = {}
    
    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    char = char.lower()
                    if char in letters:
                        letters[char] += 1
                    else:
                        letters[char] = 1
    sorted_letters = sorted(letters.items(), key = lambda x: x[1])

    if len(sorted_letters) > 0:
        final_filename = 'result_' + filename
        with open(final_filename, 'w') as final_file:
            for letter, count in sorted_letters:
                final_file.write(f"{letter}: {count}\n")
        print(f"результат записан в файл '{final_filename}'"
    else:
        print("некорректный входной файл")

filename = input("укажите имя файла ")
count_letters(filaname)
