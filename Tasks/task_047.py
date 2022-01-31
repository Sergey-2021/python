# 47. Написать программу копирования массива

def f(x):
    matrix = []
    for i in x:
        matrix.append(i)
    return matrix


m = [1, 2, 3]
t = f(m)
print(t)
