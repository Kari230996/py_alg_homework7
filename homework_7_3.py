'''
Практическая работа №7

Алгоритмы сортировки
'''
# 3) Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.

import random


def mediana(l, k):
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return l[0]

    pivot = random.choice(l)

    lesser_els = [i for i in l if i <= pivot]
    bigger_els = [i for i in l if i > pivot]
    pivots = [i for i in l if i == pivot]

    print(lesser_els)
    print(bigger_els)
    print(pivots)

    if len(lesser_els) > k:
        return mediana(lesser_els, k)
    elif len(lesser_els) + len(pivots) > k:
        return pivots[0]
    else:
        return mediana(bigger_els, k - len(bigger_els) - len(pivots))



m = 11
l = [random.randint(0, 100) for _ in range(2 + m + 1)]
print('Исхондый массив:', l)
print('Медиана данного массива:', mediana(l, m))


