# 23. Показать таблицу квадратов чисел от 1 до N

def get_square(x):
    for i in range(1, x + 1):
        print(f'{i} = {i ** 2}')


get_square(9)