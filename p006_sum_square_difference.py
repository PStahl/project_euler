#!/usr/bin/python

import math

from project_euler import timeit


def sum_square_difference(n):
    sum_of_squares = sum([n * n for n in range(1, n + 1)])
    squared_sum = int(math.pow((n * (n + 1) / 2), 2))
    return squared_sum - sum_of_squares


timeit(sum_square_difference, 100)
