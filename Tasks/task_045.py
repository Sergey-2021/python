# 45. Показать числа Фибоначчи


def fib(x):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(1,x+1):
        print(f'{a + b}  ')
        b += a
        a = b - a


fib(10)
