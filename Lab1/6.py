# Простые числа (6)
# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.

def is_prime(a):
    if(not a >= 0 or not a <= 1000):
        return 'Out of range'

    if a == 1 or a == 0:
        return False
    if a == 2:
        return True

    for i in range(2, a):
        if a % i == 0:
            return False
        else:
            return True
print(is_prime(5))