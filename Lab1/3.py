# Квадрат (3)
# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.

from math import sqrt

def square(squareSide):
    return (squareSide * 4, squareSide ** 2, squareSide * sqrt(2))

print(square(8))