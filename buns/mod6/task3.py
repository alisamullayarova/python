def is_armstrong_number(number):
    total = 0
    num_digits = len(str(number))
    temp = number
    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits
        temp //= 10
    return number == total

def get_armstrong_numbers():
    number = 10
    while True:
        if is_armstrong_number(number):
            yield number
        number += 1

armstrong_generator = get_armstrong_numbers()

for i in range(8):
    print(next(armstrong_generator), end=' ') 
