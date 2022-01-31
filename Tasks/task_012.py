# 12. Удалить вторую цифру трёхзначного числа
import random

a = random.randint(100, 1000)
print(a)

def get_new_number(x):
    x = str(x)
    y = int(x[0] + x[2])
    return y


print(get_new_number(a))
