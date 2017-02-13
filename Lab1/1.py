# Простейшие арифметические операции (1)
# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними.
# Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
# В остальных случаях вернуть строку "Неизвестная операция".

class Operations:
    def sum(self, a, b):
        return a + b
    def subtraction(self, a, b):
        return a - b
    def multiplication(self, a, b):
        return a * b
    def division(self, a, b):
        return a / b


def arithmetic(a, b, operation):
    result = Operations()

    if(operation == '+'):
        return result.sum(a, b)
    elif(operation == '-'):
        return result.subtraction(a, b)
    elif(operation == '*'):
        return result.multiplication(a, b)
    elif(operation == '/'):
        return result.division(a, b)
    else:
        return "Неизвестная операция"

print(arithmetic(1,3,'+'))
print(arithmetic(1,3,'-'))
print(arithmetic(1,3,'*'))
print(arithmetic(4,2,'/'))
print(arithmetic(4,2,'asdasd'))