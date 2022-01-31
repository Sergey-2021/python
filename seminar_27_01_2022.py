# 19. Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел
import datetime
a = datetime.datetime.now().microsecond % 10
print(a)
