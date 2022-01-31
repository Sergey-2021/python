# 4. Найти максимальное из трех чисел
x = 32
y = 4
z = 5


def GetMax(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


print(GetMax(x, y, z))
