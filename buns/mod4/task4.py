def is_palindrome(word):
    chars = {}
    for char in word:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    odd = 0
    for count in chars.values():
        if count % 2 != 0:
            odd += 1
    if odd > 1:
        return False
    else:
        return True

def make_palindrome(word):
    palindrome = ''
    chars = {}
    for char in word:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    for char, count in chars.items():
        if count % 2 == 0:
            palindrome += char * (count // 2)

    odd_char = ''
    for char, count in chars.items():
        if count % 2 != 0:
            odd_char = char
            break
    palindrome += odd_char + palindrome[::-1]
    return palindrome

word = input()
if is_palindrome(word):
    palindrome = make_palindrome(word)
    print('составленный палиндром: ', palindrome)
else:
    print('нельзя составить палиндром')
    
    
    
