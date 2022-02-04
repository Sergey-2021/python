# Составить список простых множителей натурального числа N

def f(x):
    lst = []
    a = x
    for i in range(2, x // 2 + 1):
        if i == 2 or i % 2 != 0:
            while a % i == 0:
                a /= i
                lst.append(i)

    return lst


a = 4234653
print(f(a))
