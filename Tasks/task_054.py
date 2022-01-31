# 54. В матрице чисел найти сумму элементов главной диагонали

def f(x):
    s = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            if i == j:
                s += x[i][j]
    return s


a = [[2, 2, 3],
     [4, 7, 6],
     [7, 8, 9]]
print(f(a))
