data = input('введите строку ')
count0 = 0
count1 = 0
for i in range(len(data)):
    if data[i] == '1':
        count1 += 1
    else: count0 +=1
if count0 == count1:
    print('yes')
else: print('no')
    
