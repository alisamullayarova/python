import re
import doctest

def is_correct(date: str) -> bool:
    """
    Проверка даты на соответствие условиям

    Args:
    date(str): дата

    Returns:
        bool: True - введенная дата корректна, False - некорректна

    >>> is_correct('20 января 1806')
    True
    >>> is_correct('1924, July 25')
    True
    >>> is_correct('26/09/1635')
    True
    >>> is_correct('3.1.1506')
    True
    >>> is_correct('25.08-1002')
    False
    >>> is_correct('декабря 19, 1838')
    False
    >>> is_correct('8.20.1973')
    False
    >>> is_correct('Jun 7, -1563')
    False
    >>> is_correct('31 февраля 2023')
    False
    >>> is_correct('31 июня 2015')
    False
    >>> is_correct('')
    False
    """
    format_31d = '([1-9]|[0-2]\d|3[01])'
    format_30d = '([1-9]|[0-2]\d|30)'
    format_29d = '([1-9]|[0-2]\d)'
    format_28d = '([1-9]|[01]\d|2[0-8])'
    format_31m = '(0?1|0?3|0?5|0?7|0?8|10|12)'
    format_30m = '(0?4|0?6|0?9|11)'
    format_29m = '(0?2)'
    format_28m = '(0?2)'
    year_last = -1
    if (re.split('[/.-]', date)[-1].isdigit()):
        year_last = int(re.split('[/.-]', date)[-1])
    year_first = -1
    if (re.split('[/.-]', date)[0].isdigit()):
        year_first = int(re.split('[/.-]', date)[0])

    if re.fullmatch(format_31d + '\.' + format_31m + '\.\d{1,}', date):
        return True
    if re.fullmatch(format_30d + '\.' + format_30m + '\.\d{1,}', date):
        return True
    if year_last % 4 == 0 and (year_last % 100 != 0 or year_last % 400 == 0) \
        and re.fullmatch(format_29d + '\.' + format_29m + '\.\d{1,}', date):
        return True
    elif re.fullmatch(format_28d + '\.' + format_28m + '\.\d{1,}', date):
        return True
    
    if re.fullmatch(format_31d + '/' + format_31m + '/\d{1,}', date):
        return True
    if re.fullmatch(format_30d + '/' + format_30m + '/\d{1,}', date):
        return True
    if year_last % 4 == 0 and (year_last % 100 != 0 or year_last % 400 == 0) \
        and re.fullmatch(format_29d + '/' + format_29m + '/\d{1,}', date):
        return True
    elif re.fullmatch(format_28d + '/' + format_28m + '/\d{1,}', date):
        return True
    
    if re.fullmatch(format_31d + '-' + format_31m + '-\d{1,}', date):
        return True
    if re.fullmatch(format_30d + '-' + format_30m + '-\d{1,}', date):
        return True
    if year_last % 4 == 0 and (year_last % 100 != 0 or year_last % 400 == 0) \
        and re.fullmatch(format_29d + '-' + format_29m + '-\d{1,}', date):
        return True
    elif re.fullmatch(format_28d + '-' + format_28m + '-\d{1,}', date):
        return True


    if re.fullmatch('\d{1,}\.' + format_31m + '\.' + format_31d, date):
        return True
    if re.fullmatch('\d{1,}\.' + format_30m + '\.' + format_30d, date):
        return True
    if year_first % 4 == 0 and (year_first % 100 != 0 or year_first % 400 == 0) \
        and re.fullmatch('\d{1,}\.' + format_29m + '\.' + format_29d, date):
        return True
    elif re.fullmatch('\d{1,}\.' + format_28m + '\.' + format_28d, date):
        return True
    
    if re.fullmatch('\d{1,}/' + format_31m + '/' + format_31d, date):
        return True
    if re.fullmatch('\d{1,}/' + format_30m + '/' + format_30d, date):
        return True
    if year_first % 4 == 0 and (year_first % 100 != 0 or year_first % 400 == 0) \
        and re.fullmatch('\d{1,}/' + format_29m + '/' + format_29d, date):
        return True
    elif re.fullmatch('\d{1,}/' + format_28m + '/' + format_28d, date):
        return True
    
    if re.fullmatch('\d{1,}-' + format_31m + '-' + format_31d, date):
        return True
    if re.fullmatch('\d{1,}-' + format_30m + '-' + format_30d, date):
        return True
    if year_first % 4 == 0 and (year_first % 100 != 0 or year_first % 400 == 0) \
        and re.fullmatch('\d{1,}-' + format_29m + '-' + format_29d, date):
        return True
    elif re.fullmatch('\d{1,}-' + format_28m + '-' + format_28d, date):
        return True
    

    if re.fullmatch(format_31d + ' (января|марта|мая|июня|августа|октября|декабря) ' + '\d{1,}', date):
        return True
    if re.fullmatch(format_30d + ' (апреля|июля|сентября|ноября) ' + '\d{1,}', date):
        return True
    if year_first % 4 == 0 and (year_first % 100 != 0 or year_first % 400 == 0) \
        and re.fullmatch(format_29d + ' февраля ' + '\d{1,}', date):
        return True
    elif re.fullmatch(format_28d + ' февраля ' + '\d{1,}', date):
        return True
    
    if re.fullmatch('(January|March|May|July|August|October|December) ' + format_31d + ', \d{1,}', date):
        return True
    if re.fullmatch('(April|June|September|November) ' + format_30d + ', \d{1,}', date):
        return True
    if year_first % 4 == 0 and (year_first % 100 != 0 or year_first % 400 == 0) \
        and re.fullmatch('February ' + format_29d + ', \d{1,}', date):
        return True
    elif re.fullmatch('February ' + format_28d + ', \d{1,}', date):
        return True
    
    if re.fullmatch('(Jan|Mar|May|Jul|Aug|Oct|Dec) ' + format_31d + ', \d{1,}', date):
        return True
    if re.fullmatch('(Apr|Jun|Sep|Nov) ' + format_30d + ', \d{1,}', date):
        return True
    if year_first % 4 == 0 and (year_first % 100 != 0 or year_first % 400 == 0) \
        and re.fullmatch('Feb ' + format_29d + ', \d{1,}', date):
        return True
    elif re.fullmatch('Feb ' + format_28d + ', \d{1,}', date):
        return True
    
    if re.fullmatch('\d{1,}, ' + '(January|March|May|July|August|October|December) ' + format_31d, date):
        return True
    if re.fullmatch('\d{1,}, ' + '(April|June|September|November) ' + format_30d, date):
        return True
    if year_first % 4 == 0 and (year_first % 100 != 0 or year_first % 400 == 0) \
        and re.fullmatch('\d{1,}, ' + 'February ' + format_29d, date):
        return True
    elif re.fullmatch('\d{1,}, ' + 'February ' + format_28d, date):
        return True
    
    if re.fullmatch('\d{1,}, ' + '(Jan|Mar|May|Jul|Aug|Oct|Dec) ' + format_31d, date):
        return True
    if re.fullmatch('\d{1,}, ' + '(Apr|Jun|Sep|Nov) ' + format_30d, date):
        return True
    if year_first % 4 == 0 and (year_first % 100 != 0 or year_first % 400 == 0) \
        and re.fullmatch('\d{1,}, ' + 'Feb ' + format_29d, date):
        return True
    elif re.fullmatch('\d{1,}, ' + 'Feb ' + format_28d, date):
        return True
    
doctest.testmod()