# Времена года (4)
# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).

def season(monthNumber):
    if(monthNumber >= 1 and monthNumber < 3 or monthNumber == 12):
        return ('зима')
    elif(monthNumber >= 3 and monthNumber < 6):
        return ('весна')
    elif(monthNumber >= 6 and monthNumber < 9):
        return ('лето')
    elif(monthNumber >= 9 and monthNumber < 12):
        return ('осень')
    else:
        return ('неверные данные')

print(season(8))