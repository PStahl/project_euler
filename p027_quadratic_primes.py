#!/usr/bin/python

from gmpy import is_prime

from project_euler import timeit


def f(a, b, n):
    return n * n + a * n + b


def quadratic_primes(limit_a, limit_b):
    max_so_far = 0
    a = -limit_a + 1
    while a < limit_a:
        b = -limit_b + 1
        while b < limit_b:
            n = 0
            while is_prime(f(a, b, n)):
                n += 1
            if n > max_so_far:
                max_so_far = n
                a_and_b = (a, b)
            b += 1
        a += 1

    (a, b) = a_and_b
    return a * b


timeit(quadratic_primes, 1000, 1000)
