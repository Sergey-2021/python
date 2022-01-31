# 28. Подсчитать сумму цифр в числе

number = input('Введите число ')


def get_sum(x):
    sum = 0
    for i in x:
        sum += int(i)
    return sum


print(get_sum(number))
