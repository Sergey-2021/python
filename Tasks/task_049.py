# 49. Показать двумерный массив размером m×n заполненный вещественными числами
import random


def f(m, n):
    matrix = []
    for i in range(m):
        matrix.append([])
        for j in range(n):
            matrix[i].append(random.random())
    return matrix


a = 3
b = 4
print(f(a, b))
