number = float(input())
binary = ''
octal = ''
hexadecimal = ''
hex_symbols = "0123456789ABCDEF"
if number % 1 != 0 or number <= 0:
    print("Неверный ввод")
else:
    number1 = int(n)
    number2 = int(n)
    number3 = int(n)
    if number <= 0:
        print("Неверный ввод")
    else:
        while number1 > 0:
            binary = str(number1 % 2) + binary
            number1 = number1 // 2
        while number2 > 0:
            octal = str(number2 % 8) + octal
            number2 = number2 // 8
        while number3 > 0:
            hexadecimal = hex_symbols[number3 % 16] + hexadecimal
            number3 = number3 // 16
print(binary, octal, hexadecimal)

