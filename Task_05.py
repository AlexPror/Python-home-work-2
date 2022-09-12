# Задача 5. Реализуйте алгоритм перемешивания списка.
import random
def mixList(list):
    random.shuffle(list)
    print(f'Перемешанный список: {list}')

list = ['lenovo', 'ideapad320', 'amd10', 'radeon 5']
print(f'Исходный список: {list}')
res = mixList(list)
