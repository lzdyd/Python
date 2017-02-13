# Правильная дата (7)
# Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True,
# если такая дата есть в нашем календаре, и False иначе.

def date(d, m, y):
    if(d <= 0 or d >= 32 or m <= 0 or m >= 13 or y <= 0):
        return False

    if (is_year_leap(y) and m == 2):
        if (d <= 29):
            return True
        else:
            return False

    if(m == 2):
        if(d <= 28):
            return True
        else:
            return False

    if(m % 2 == 0):
        return evenMonths(d)
    if (m % 2 != 0):
        return oddMonths(d)


def is_year_leap(year):
    if (not year % 4 and year % 100) or not year % 400:
        return True
    else:
        return False

def evenMonths(d):
    if(d > 0 and d <= 30):
        return True
    else:
        return False

def oddMonths(d):
    if(d > 0 and d <= 31):
        return True
    else:
        return False

print(date(29, 2, 2012))
print(date(29, 2, 2013))