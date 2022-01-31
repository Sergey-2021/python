# 14. Найти третью цифру числа или сообщить, что её нет
a = 394567


def r(x):
    d = str(x)
    if x > 0 and len(d) >= 3:
        return int(d[2])
    elif x < 0:
        return int(d[3])
    else:
        return 'ее нет'


print(r(a))
