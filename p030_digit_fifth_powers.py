#!/usr/bin/python

import math

from project_euler import timeit

cache = {}


def digit_powers(n):
    lower_limit = 2
    upper_limit = n * int(math.pow(9, n))

    return sum([x for x in range(lower_limit, upper_limit + 1) if is_power_sum(n, x)])


def is_power_sum(n, nbr):
    digits = [int(x) for x in str(nbr)]
    for d in digits:
        if d in cache.keys():
            nbr -= cache[d]
        else:
            cache[d] = int(math.pow(d, n))
            nbr -= cache[d]

        if n < 0:
            return False

    return nbr == 0


timeit(digit_powers, 5)
