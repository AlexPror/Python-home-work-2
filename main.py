# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 0,56 -> 11

def sumFloatNum(num):
    newList = [int(i) for i in num if i != '.']
    sum = 0
    for i in range(len(newList)):
        sum += newList[i]
    return sum

num = input('Пожалуйста, введите вещественное число для подсчета суммы цифр в числе: ')
sumRes = sumFloatNum(num)
print(f"Сумма цифр в числе: {sumRes}")