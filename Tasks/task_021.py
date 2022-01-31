# 21. Программа проверяет пятизначное число на палиндромом.

def yr(x):
    x = str(x)
    return x[0] == x[4] and x[1] == x[3]


a = int(input('a= '))
print(yr(a))
