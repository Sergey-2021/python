# 13. Выяснить, кратно ли число заданному, если нет, вывести остаток.

a = int(input('a= '))
b = int(input('b= '))

def tg(x, y):
    if a % b == 0:
        return True
    else:
        return a % b


print(tg(a, b))
