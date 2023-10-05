data = input()
word = ''
for i in range(len(data)):
    if data[i] == ' ':
        word = word + data[i - 1]

print(word + data[len(data) - 1])
