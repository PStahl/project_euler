#!/usr/bin/python

import math

from project_euler import timeit


def is_curious(cache, n):
    factorial_sum = sum([cache[int(x)] for x in str(n)])
    return n == factorial_sum


def digital_factorials():
    cache = [math.factorial(i) for i in range(10)]
    result = sum([i for i in range(10, math.factorial(i)) if is_curious(cache, i)])
    return result


timeit(digital_factorials)
