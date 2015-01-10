#!/usr/bin/python

import sys

from collections import Counter

from project_euler import timeit, is_pandigital


def concatenated(l):
    return reduce(lambda x, y: str(x) + str(y), l)


def pandigital_multiples(upper_limit):
    max_so_far = -sys.maxint

    for i in range(1, upper_limit):
        t = [1, 2]
        nbr = concatenated(map(lambda x: x * i, t))
        while len(nbr) < 10:
            if is_pandigital(nbr):
                max_so_far = max(max_so_far, int(nbr))
            
            t.append(t[-1] + 1)
            nbr = concatenated(map(lambda x: x * i, t))

    return max_so_far


timeit(pandigital_multiples, 9999)
