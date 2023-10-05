data = input()
for i in range(len(data)):
    if data[i] == ",":
        break

string = data[:i]
symbol = data[i + 1:]

count = 0

for j in range(len(string)):
    if string[j] == symbol:
        count += 1
    if string[j] != string[j + 1]:
        break

print(count)
