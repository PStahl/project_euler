#!/usr/bin/python

from project_euler import timeit
from gmpy import is_prime


def corner_primes(n):
    last = (n * 2 + 1) ** 2
    return sum([1 for i in range(4) if is_prime(last - i * 2 * n)])



def spiral_primes(limit):
    ratio = 100.0
    layer = 1
    primes = 0
    total = 1
    while 100 * ratio > limit:
        layer += 1
        primes += corner_primes(layer)
        total += 4
        ratio = float(primes) / total

    return (layer - 1) * 2 + 1


timeit(spiral_primes, 10.0)
