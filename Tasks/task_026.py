# Возведите число А в натуральную степень B используя цикл

def f(x, y):
    c = 1
    for i in range(y):
        c *= x
    return c


number = 2
degree = 20

a = f(number, degree)
b = a / 1024
print(b)

