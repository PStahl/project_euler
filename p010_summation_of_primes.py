#!/usr/bin/python

from project_euler import timeit, get_primes_under_n


def sum_of_primes(n):
    return sum(get_primes_under_n(n))


timeit(sum_of_primes, 2000000)
