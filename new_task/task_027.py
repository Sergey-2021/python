# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

def f(x):
    c = [int(i) for i in x.split(' ')]
    r = max(c)
    n = min(c)
    return f'min= {n}, max= {r}'


a = '1 2 3 4 5 6 7 8 9'
print(f(a))


