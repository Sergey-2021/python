# 27. Определить количество цифр в числе

def f(x):
    count = 0
    x = str(x)
    for i in range(len(x)):
        count += 1
    return count


a = 8415637
print(f(a))
