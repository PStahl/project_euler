#!/usr/bin/python

import sys
import math

from project_euler import timeit


def is_pentagonal(n):
    p = (math.sqrt(24 * n + 1) + 1) / 6
    return p == int(p)


def pentagon(n):
    return n * (3 * n - 1) / 2


def minimal_pentagon_numbers_sum():
    j = 1
    k = 2

    min_so_far = sys.maxint

    pk = pentagon(k)
    pj = pentagon(j)

    found = False
    while not found:
        j = k - 1
        while j > 0:
            pj = pentagon(j)
            sum = pk + pj
            diff = pk - pj
            if is_pentagonal(sum) and is_pentagonal(diff) and diff < min_so_far:
                min_so_far = diff
                found = True

            j -= 1

        k += 1
        pk = pentagon(k)

    return min_so_far


timeit(minimal_pentagon_numbers_sum)
