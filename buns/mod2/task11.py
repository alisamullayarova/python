data = input()
out = False
while 1:
    for i in range(0, len(data)):
        for j in range(0, len(data)):
            if i != j:
                if data[i] == data[j] and data[i] != " ":
                    out = True
                    break
    break
print(out)
