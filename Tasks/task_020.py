# 20. Задать номер четверти, показать диапазоны для возможных координат



x = int(input('x= '))
y = int(input('y= '))


def get_quarter(a, b):
    quarters = ['Первая четверть', 'Вторая четверть', 'Третья четверть', 'Четвертая четверть']
    if a > 0 and b > 0:
        return quarters[0] + ' ' + 'X(от 0 до N) и Y(от 0 до N)'
    elif a < 0 and b > 0:
        return quarters[1] + ' ' + 'X(от -N до 0) и Y(от 0 до N)'
    elif a < 0 and b < 0:
        return quarters[2] + ' ' + 'X(от -N до 0) и Y(от -N до 0)'
    else:
        return quarters[3] + ' ' + 'X(от 0 до N) и Y(от -N до 0)'


print(get_quarter(x, y))
