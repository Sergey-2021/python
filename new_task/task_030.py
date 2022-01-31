# Вычислить число  c заданной точностью d
# 	Пример: при d = 0.001,  = 3.141.  10-1d10-10
import math


def f(x):
    a = str(x)
    b = str(math.pi)
    c = ''
    i = 0
    while i != len(a):
        c = c+b[i]
        i += 1
    return float(c)


d = 0.001
print(f(d))
