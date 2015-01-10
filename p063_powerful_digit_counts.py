#!/usr/bin/python

import math

from project_euler import timeit


def powerful_digit_counts():
    n = 1
    lower = 1
    cnt = 0
    while lower < 10:
        lower = int(math.ceil(math.pow(10, (n - 1.0) / n)))
        cnt += (10 - lower)
        n += 1

    return cnt


timeit(powerful_digit_counts)
