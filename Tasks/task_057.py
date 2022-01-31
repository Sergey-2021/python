# 57. Написать программу, упорядочивания по убыванию элементы каждой строки двумерной массива

def f(x):
    for i in range(len(x)):
        x[i].sort(reverse=True)
    return x


list_1 = [[4, 7, 3], [9, 5, 7], [6, 10, 1]]
print(f(list_1))

