# 19. Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0

x = int(input('x= '))
y = int(input('y= '))


def get_quarter(a, b):
    quarters = [1, 2, 3, 4]
    if a > 0 and b > 0:
        return quarters[0]
    elif a < 0 and b > 0:
        return quarters[1]
    elif a < 0 and b < 0:
        return quarters[2]
    else:
        return quarters[3]


print(get_quarter(x, y))
