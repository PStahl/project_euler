#!/usr/bin/python

from project_euler import timeit, get_primes_under_n


def largest_prime_factor(n):
    primes = get_primes_under_n(n)
    return max([prime for prime in primes if n % prime == 0])


n = 600851475143
timeit(largest_prime_factor, n)
