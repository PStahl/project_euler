#!/usr/bin/python

import sys

from itertools import combinations

from project_euler import timeit, get_primes_under_n


def get_number_of_distinct_prime_factors(primes, n):
    count = 0
    f = 2
    factors = set()
    for p in primes:
        if p > n:
            break
        elif n % p == 0 and p not in factors:
            count += 1
            factors.add(p)

    return count


def smallest_distinct_prime_factors(number_of_factors, upper_bound):
    primes = get_primes_under_n(1000)
    print len(primes)
    nbr = 2 * 3 * 5 * 7
    cnt = 1

    while cnt != number_of_factors:
        nbr += 1
        if get_number_of_distinct_prime_factors(primes, nbr) == number_of_factors:
            cnt += 1
        else:
            cnt = 0

    return nbr - number_of_factors + 1


timeit(smallest_distinct_prime_factors, 4, 1000)
