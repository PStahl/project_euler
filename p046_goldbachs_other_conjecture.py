#!/usr/bin/python

import math

sieve = [True] * 10000 # Sieve is faster for 2M primes
def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]: mark(sieve, x)

composites = [i for i in xrange(2, len(sieve)) if not sieve[i] and not i % 2 == 0]
primes = [i for i in xrange(2, len(sieve)) if sieve[i]]
sum_squares = [p + 2*i*i for p in primes for i in range(1, 100)]

for c in composites:
    if not c in sum_squares:
        print c
        break





