'''
Практическая работа №7

Алгоритмы сортировки
'''
# 2) Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
from random import randint


def merge_sort(num):

    if len(num) > 1:

        middle = len(num) // 2

        left_half = num[:middle]
        right_half = num[middle:]

        merge_sort(left_half)
        merge_sort(right_half)

        i=0
        j=0
        k=0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                num[k] = left_half[i]
                i += 1
            else:
                num[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            num[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            num[k] = right_half[j]
            j += 1
            k += 1



N = 10
num = [randint(0, 50) for i in range(N)]
merge_sort(num)

print('Отсортированный список по возрастанию методом слияния:', num)
