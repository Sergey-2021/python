# 17. По двум заданным числам проверять является ли одно квадратом другого

def rt(a, b):
    return a * a == b or b * b == a


x = int(input('x= '))
y = int(input('y= '))

print(rt(x, y))
