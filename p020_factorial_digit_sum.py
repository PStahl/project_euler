#!/usr/bin/python2.7

from project_euler import timeit


def digit_sum(n):
    factorial = 1
    i = 2

    while i <= n:
        factorial *= i
        if factorial % 10 == 0:
            factorial = factorial / 10
        i += 1

    nbrs = map(lambda x: int(x), str(factorial))
    return sum(nbrs)


timeit(digit_sum, 100)
