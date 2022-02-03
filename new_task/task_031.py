# Составить список простых множителей натурального числа N

def f(x):
    lst = []
    a = x
    for i in range(2, x//9):
        if i == i:
            while a % i == 0:
                a = a / i
                lst.append(i)

    return lst


a = 45012324

print(f(a))
