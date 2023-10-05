data = input()
even = 0
odd = 0
for i in range(len(data)):
    if i % 2 == 0:
        odd += int(data[i])
    else: even += int(data[i])

if (odd + even * 3) % 10 == 0:
    print('yes')
else: print('no')    

