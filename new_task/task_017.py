# 17.Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

def f(x):
    with open('File.txt', 'w') as data:
        for i in range(-x, x + 1):
            data.write(f'{i}\n')


def t(a, b):
    with open('File.txt', 'r') as data:
        count = 0
        for i in data:
            count += 1
            if count == a:
                a = int(i)
            if count == b:
                b = int(i)
    return a * b


n = 10
f(n)
position_1 = 1
position_2 = 12
print(t(position_1, position_2))
