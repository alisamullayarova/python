def euclid_alg(num1, num2):
    if num1 == 0 or num2 == 0:
        return None
    elif num1 == num2:
        return num1
    elif num1 > num2:
        if num1 % num2 == 0:
            return num2
        else:
            num1 = num1 - num2
            return euclid_alg(num1,  num2)
    elif num2 > num1:
        if num2 % num1 == 0:
            return num1
        else:
            num2 = num2 - num1
            return euclid_alg(num1,  num2)
        

num1 = int(input('введите первое число '))
num2 = int(input('введите второе число '))
print(euclid_alg(num1, num2))
        
