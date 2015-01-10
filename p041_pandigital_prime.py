#!/usr/bin/python

from collections import Counter
from itertools import permutations

from project_euler import timeit, sieves


def largest_pandigital_prime(sieve):
    for i in xrange(7, 1, -1):
        for perm in permutations([7, 6, 5, 4, 3, 2, 1], i):
            if sieve[to_int(perm)]:
                return to_int(perm)


def is_pandigital(d, n):
    if len(str(d)) < n:
        return False

    count = Counter([str(i) for i in range(1, n + 1)])

    return count == Counter(str(d))


def to_int(n):
    return int(reduce(lambda rst, d: rst * 10 + d, n))


timeit(largest_pandigital_prime, sieves(7654322))
