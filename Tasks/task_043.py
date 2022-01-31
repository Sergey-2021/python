# 43. Написать программу преобразования десятичного числа в двоичное

def tt(x):
    f = ''
    while x > 0:
        f += str(x % 2)
        x = int(x / 2)
    f = f[::-1]
    return f


a = 10
print(tt(a))
