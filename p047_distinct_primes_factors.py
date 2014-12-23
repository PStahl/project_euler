#!/usr/bin/python

import sys
from itertools import combinations

sieve = [True] * 1000 # Sieve is faster for 2M primes
def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]: mark(sieve, x)

primes = [i for i in xrange(2, len(sieve)) if sieve[i]]

def get_distinct_prime_factors(n):
    f = 2
    factors = set()
    for p in primes:
        if p > n:
            break
        elif n % p == 0:
            factors.add(p)

    return list(factors)


result = []
n = 2 * 3 * 5 * 7
nf = 4
ns = 4
ci = 1

while ci != ns:
    n += 1
    if len(get_distinct_prime_factors(n)) == nf:
        ci += 1
    else:
        ci = 0

print n
