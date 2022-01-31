# 30. Показать кубы чисел, заканчивающихся на четную цифру

def get_even_number(x):
    for i in range(1, x + 1):
        if i % 2 == 0:
            print(i ** 3)


a = 9
get_even_number(a)
