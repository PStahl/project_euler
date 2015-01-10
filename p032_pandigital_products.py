#!/usr/bin/python

from collections import Counter

from project_euler import timeit


UPPER_LIMIT = 9999 # 1 x 9999 = 9999 == 9 digits
DIGITS = Counter("123456789")


def is_unusual(a, b, c):
    s = str(a) + str(b) + str(c)
    if len(s) > 9:
        return False

    return DIGITS == Counter(s)


def pandigital_products():
    unusual = set()
    for i in range(2, 100):
        j_begin = 123 if i > 9 else 1234
        j_end = 10000 / (i + 1)
        for j in range(j_begin, j_end):
            if is_unusual(i, j, i * j):
                unusual.add(i * j)

    return sum(unusual)


timeit(pandigital_products)
