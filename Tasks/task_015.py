# 15. Дано число. Проверить кратно ли оно 7 и 23
def it(x):
    return x % 7 == 0 and x % 23 == 0


a = int(input('a= '))
print(it(a))
