#!/usr/bin/python

from project_euler import timeit


def even_fibs(n):
    fibs = [1, 1]
    while fibs[-1] < n:
        fibs.append(fibs[-1] + fibs[-2])

    return sum(filter(lambda x: x % 2 == 0, fibs))


timeit(even_fibs, 4000000)
