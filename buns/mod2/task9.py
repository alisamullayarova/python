data  = input()
vowels = 0
consonants = 0
for i in range(len(data)):
    if data[i] != 'ъ' and data[i] != 'ь' and data[i] != ' ':
        if data[i] == 'а' or data[i] == 'я' or data[i] == 'о' or data[i] == 'ё' or data[i] == 'у' or data[i] == 'ю' or data[i] == 'э' or data[i] == 'е' or data[i] == 'ы' or data[i] == 'и':
            vowels += 1
        else: consonants += 1
print(vowels, consonants)
