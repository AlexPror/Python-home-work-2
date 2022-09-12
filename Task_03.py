# Задача 3. Задайте список из k чисел последовательности
# (1 + 1\k)^k и выведите на экран их сумму.

def sequence(k):
    list = []
    list1 = [(list.append(round((1 + 1/i) ** i, 2))) for i in range(1, k+1)]
    return list

def sequenceSum(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum
k = (int(input('Задайте количество элементов : ')))
list = sequence(k)
result = sequenceSum(list)
print(list)
print(f"Сумма значений : {result}")