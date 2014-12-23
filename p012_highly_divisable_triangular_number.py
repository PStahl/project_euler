#!/usr/bin/python

import itertools

from project_euler import timeit, get_n_primes, prime_factorisation_no

def triangular_number(n):
    primes = get_n_primes(1000)
    i = 1
    cnt = 0
    Dn1 = 2
    Dn = 2
    N = 500

    while cnt < N:
        if i % 2 == 0:
            Dn = prime_factorisation_no(i + 1, primes)
            cnt = Dn * Dn1
        else:
            Dn1 = prime_factorisation_no((i + 1) / 2, primes)
            cnt = Dn*Dn1
        i += 1

    number = i * (i - 1) / 2
    return number


timeit(triangular_number, 500)
