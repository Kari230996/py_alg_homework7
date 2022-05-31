'''
Практическая работа №7

Алгоритмы сортировки
'''
# 1) Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы

import random
import timeit

SIZE = 10
lst = [random.randint(-100, 99) for i in range(SIZE)]



def bubble_sort():

    n = len(lst)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


    return f'Отсортированный список по убыванию: {lst}'

print(bubble_sort())
print(timeit.timeit('bubble_sort()', number=100, globals=globals())) # SIZE = 1000, 3.1406147999987297


'''Оптимизация'''

def updated_bubble_sort():

    n = len(lst)

    for i in range(n - 1):
        flag = True
        for j in range(n - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

                flag = False

        if flag:
            break


    return f'Отсортированный список по убыванию: {lst}'

print(updated_bubble_sort())
print(timeit.timeit('updated_bubble_sort()', number=100, globals=globals())) # SIZE = 1000, 0.012496100003772881


