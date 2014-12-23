#!/usr/bin/python

from collections import Counter

sieve = [True] * 10000000 # Sieve is faster for 2M primes
def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]: mark(sieve, x)

def is_pandigital(d, n):
    if len(str(d)) < n:
        return False

    count = Counter([str(i) for i in range(1, n + 1)])

    return count == Counter(str(d))

primes = [i for i in xrange(2, len(sieve)) if sieve[i] and is_pandigital(i, len(str(i)))]

print primes
print max(primes)
