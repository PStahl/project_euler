#!/usr/bin/python

import math
from project_euler import timeit, get_primes_under_n


def smallest_multiple(n):
    primes = get_primes_under_n(n)
    result = 1
    for prime in primes:
        a = int(math.floor(math.log(n) / math.log(prime)))
        result *= int(math.pow(prime, a))

    return result


timeit(smallest_multiple, 20)
