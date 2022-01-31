import random
print(random.randint(24, 60))
#  7 .Показать числа от -N до N
# N = 4
# def get_t(v):
#     s = 1
#     for i in range(1, N+1):
#         s *= i
#     return s
# print(get_t(N))
# 18.Проверить истинность утверждения ¬(X ⋁ Y Z) = ¬X ⋀ ¬Y ¬Z
# def Tf(x, y ,z):
#     return not(x or y or z) == (not x and not y and not z)
# print(Tf(0, 1, 0))