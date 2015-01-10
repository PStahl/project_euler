#!/usr/bin/python

from project_euler import timeit


def spiral_diagonals(m):
    total = 1
    for n in xrange(3, m + 1, 2):
        total += 4 * n ** 2 - 6 * (n - 1)

    return total


timeit(spiral_diagonals, 1001)
