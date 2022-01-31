# 6. Выяснить является ли число чётным

a = int(input('a = '))


def even_number(x):
    c = x % 2 == 0
    return c


b = even_number(a)

print(b)
