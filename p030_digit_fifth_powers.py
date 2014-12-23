#!/usr/bin/python

import math

N = 5
LOWER_LIMIT = 2
UPPER_LIMIT = N * int(math.pow(9, N))

cache = {}

def is_power_sum(n):
    digits = [int(x) for x in str(n)]
    for d in digits:
        if d in cache.keys():
            n -= cache[d]
        else:
            cache[d] = int(math.pow(d, N))
            n -= cache[d]

        if n < 0:
            return False

    return n == 0

sum = sum([x for x in range(LOWER_LIMIT, UPPER_LIMIT + 1) if is_power_sum(x)])

print sum



