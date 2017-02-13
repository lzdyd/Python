# Високосный год (2)
# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.

def is_year_leap(year):
    if (not year % 4 and year % 100) or not year % 400:
        return True
    else:
        return False

print(is_year_leap(2000))
