# 16. Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму

def f(n):
    t = [(1+1*i)*i for i in range(1, 6)]
    return sum(t)


x = 6
print(f(x))
