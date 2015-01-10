#!/usr/bin/python

import math

from project_euler import timeit


def distinct_powers(low, high):
    numbers = set()

    for a in range(low, high + 1):
        prev = a
        for b in range(low, high + 1):
            numbers.add(prev * a)
            prev = prev * a

    return len(list(numbers))


timeit(distinct_powers, 2, 100)
