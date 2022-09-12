# Задача 2. Напишите программу, которая принимает на вход число
# N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def listForFactorial(num):
    list = []
    for i in range(num):
        i += 1
        list.append(i)
    return list

def factorial(num):
    list2 =[]
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
        num -= 1
        list2.append(factorial)
    return list2

num = (int(input('Задайте количество элементов списка:')))
list = listForFactorial(num)
print(list)
list2 = factorial(num)
print(list2)
