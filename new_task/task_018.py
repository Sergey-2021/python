# Реализовать алгоритм перемешивания списка.

def f(x):
    for i in range(len(x) // 2):
        x.append(x[i])
        x.remove(x[i])
    return x


l_1 = ['w', 's', 7, 4, 5, 6, 1, 3]
print(f(l_1))
