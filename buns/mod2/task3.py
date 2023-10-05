numbers = input()
div_point1 = numbers.find(" ")
a = int(numbers[:div_point1])
div_point2 = numbers.find(" ", div_point1+1)
b = int(numbers[div_point1+1:div_point2])
c = int(numbers[div_point2+1:])
if (a > b):
    if (c > a): print(a)
    elif (c > b): print(c)
    else:print(b)
elif(c > b):print(b)
else:
    if (a > c):print(a)
    else: print(c)
