

# 51. Задать двумерный массив следующим правилом: Aₘₙ = m+n


def f(m, n):
    matrix = []
    for i in range(m):
        matrix.append([])
        for j in range(n):
            matrix[i].append(i+j)
    return matrix


a = 3
b = 4
print(f(a, b))
