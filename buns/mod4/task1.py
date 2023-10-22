def check(numbers):
    different = set(numbers)
    if len(different) == 1:
        return 'Все числа равны'
    elif len(different) == len(numbers):
        return 'Все числа разные'
    else:
        return 'Есть равные и неравные числа'

length = int(input('введите длину списка '))
data = [int(input('введите число')) for _ in range(length)]
print(check(data))
