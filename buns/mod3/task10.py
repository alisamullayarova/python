data = int(input())
for i in range(1, data + 1):
    for j in range(1, data + 1):
        if j!= data:
            print(j, end = ',')
        else:
            print(j)
print()
for i in range(1, data + 1):
    for j in range(1, data + 1):
        if j!= data:
            print(i, end = ',')
        else:
            print(i)

