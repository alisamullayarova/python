def raiser(a, n):
    if n == 0:
        return 1
    elif n % 2 ==  0:
        return raiser(a * a, n //2)
    else:
        return a * raiser(a, n - 1)

a = int(input('введите число '))
n = int(input('введите степень '))
print(raiser(a, n))
