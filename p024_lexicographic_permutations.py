#!/usr/bin/python

from project_euler import timeit

import itertools


def lexicographic_permutations(n):
    nbrs = [str(unichr(x + ord('0'))) for x in range(0, 10)]
    permutations = itertools.permutations(nbrs)
    return "".join(list(permutations)[n - 1])


timeit(lexicographic_permutations, 1000000)
