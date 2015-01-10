#!/usr/bin/python

from project_euler import timeit, sieves


def circular_nbrs(i):
    s = str(i)
    nbrs = []
    for i in range(len(s)):
        nbrs.append(int(s[i:] + s[0:i]))
    return nbrs


def is_circular(sieve, i):
    return all(sieve[n] for n in circular_nbrs(i))


def circular_primes(n):
    sieve = sieves(n)
    primes = [i for i in xrange(2, len(sieve)) if sieve[i] and is_circular(sieve, i)]
    return len(primes)


timeit(circular_primes, 1000000)
