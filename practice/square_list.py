import math


def range_square(n, m):
    lst = []
    for i in range(n, m):
        lst.append(i ** 2)
    return lst


print(range_square(2, 31))
