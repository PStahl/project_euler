#!/usr/bin/python

from project_euler import timeit


def cycle_length(d):
    if not isinstance(d, int) or d <= 0:
        raise ValueError("cycle_length(d): d must be a positive integer")

    rlist = []
    qlist_len = 0
    remainder = 1

    while remainder:
        remainder = remainder % d
        if remainder in rlist:
            return qlist_len - rlist.index(remainder)
        rlist.append(remainder)
        remainder *= 10
        qlist_len+=1

    return 0


def reciprocal_cycles(n):
    max_so_far = 0
    max_d = 0
    for d in range(2, n):
        length = cycle_length(d)
        if length > max_so_far:
            max_so_far = length
            max_d = d


    return max_d


timeit(reciprocal_cycles, 1000)
