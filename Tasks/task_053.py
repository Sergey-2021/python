# 53. В двумерном массиве показать позиции числа, заданного пользователем или указать, что такого элемента нет

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def get_position(x, b):
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == b:
                return f'[{i}][{j}]'
    else:
        return 'No number'


a = int(input('a= '))
print(get_position(matrix, a))
