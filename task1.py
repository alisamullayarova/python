import re
import doctest

def is_correct(password: str) -> bool:
    """
    Проверка пароля на соответствие условиям

    Args:
    password(str): Пароль

    Returns:
        bool: True - введенный пароль корректен, False - некорректен

    >>> is_correct('rtG&3FG#Tr^e')
    True
    >>> is_correct('a^A1@*@1Aa')
    True
    >>> is_correct('oF^a1D@y5%e6')
    True
    >>> is_correct('enroi#$*rkdeR#$*092uwedchf34tguv394h')
    True
    >>> is_correct('пароль')
    False
    >>> is_correct('password')
    False
    >>> is_correct('qwerty')
    False
    >>> is_correct('lOngPa$$W0R')
    False
    >>> is_correct('nduvDTng@&%??')
    False
    >>> is_correct('5356')
    False
    >>> is_correct('PNNvdPMNVV')
    False
    """

    # только лат.буквы, цифры и спец.символы
    if not re.match(r'^[a-zA-Z0-9^$%@#&*!?]+$', password):
        return False
    # длина не меньше 8
    if len(password) < 8:
        return False
    # не менее 2 лат.букв в нижнем регистре
    if len(re.findall(r'[a-z]', password)) < 2:
        return False
    # цифры
    if not re.search(r'\d', password):
        return False
    # не менее 3 различных спец.символов
    if len(set(re.findall(r'[^a-zA-Z0-9]', password))) < 3:
        return False
    # не содержит .,!?
    if re.search(r'[,.!?]', password):
        return False
    return True

doctest.testmod()