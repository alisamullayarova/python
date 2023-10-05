data = input('введите числа: ')
c = 0
for i in range(len(data)):
    if data[i] == " ":
        c = i
        break

a = int(data[:i - 1])
b = int(data[i + 1:])
print(a % b)
