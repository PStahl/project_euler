#!/usr/bin/python

import math

from project_euler import timeit, sieves


def smallest_non_composite(upper_bound):
    sieve = sieves(upper_bound)
    composites = [i for i in xrange(2, len(sieve)) if not sieve[i] and not i % 2 == 0]
    primes = [i for i in xrange(2, len(sieve)) if sieve[i]]
    sum_squares = [p + 2*i*i for p in primes for i in range(1, 100)]

    for nbr in composites:
        if not nbr in sum_squares:
            return nbr


timeit(smallest_non_composite, 10000)
