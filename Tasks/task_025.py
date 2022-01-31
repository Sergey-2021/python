# 25. Найти сумму чисел от 1 до А
import random

a = random.randint(1, 10)
print(a)


def get_summa(x):
    summa = 0
    for i in range(1, x + 1):
        summa += i
    return summa


print(get_summa(a))
