# 18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

def dr(x, y):
    return not(x or y) == (not x and not y)


a = 34
b = 6

print(dr(a, b))
