# 22. Найти расстояние между точками в пространстве 2D/3D
x1 = 2
y1 = 5
x2 = 4
y2 = 2


def get_interval(a1, b1, a2, b2):
    interval = pow((a2 - a1) ** 2 + (b2 - b1) ** 2, 0.5)
    return interval


print(round(get_interval(x1, y1, x2, y2), 2))
