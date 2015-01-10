#!/usr/bin/python

import sys

from project_euler import timeit, sieve_and_primes


def consecutive_prime_sum(upper_bound):
    (sieve, primes) = sieve_and_primes(upper_bound)

    max_so_far = - sys.maxint
    longest_so_far = 0

    for index, prime in enumerate(primes):
        i = 1
        prime_sum = prime
        while index + i < len(primes) and prime_sum < upper_bound:
            if i >= longest_so_far and sieve[prime_sum]:
                longest_so_far = i
                max_so_far = prime_sum

            prime_sum += primes[index + i]
            i += 1

    return max_so_far


timeit(consecutive_prime_sum, 1000000)
