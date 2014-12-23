#!/usr/bin/python2.7

import math

from project_euler import timeit


def power_digit_sums(n):
    n = int(math.pow(2, n))

    digits = map(lambda x: int(x), str(n))
    return sum(digits)


timeit(power_digit_sums, 1000)
