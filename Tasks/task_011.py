# 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

a = int(input('a= '))


def get_max_element(x):
    x = str(x)
    if x[0] > x[1]:
        return int(x[0])
    else:
        return int(x[1])


print(get_max_element(a))
