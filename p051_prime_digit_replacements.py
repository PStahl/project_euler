#!/usr/bin/python
import sys
import itertools

def is_prime(n):
    if any(n % p == 0 for p in primes):
        return True
    else:
        return False

sieve = [True] * 10000000 # Sieve is faster for 2M primes
def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]: mark(sieve, x)


primes = [p for p in range(56000, 2000000) if sieve[p]]


def transform_number(number, positions, nbr):
    for pos in positions:
        number = number[:pos] + str(nbr) + number[pos + 1:]

    if len(str(int(number))) < len(number):
        return 4 # non-prime

    return int(number)

def number_of_primes(number, positions):
    if not positions:
        return 0

    n = [transform_number(number, positions, nbr) for nbr in range(0, 10) if sieve[transform_number(number, positions, nbr)]]
    if n:
        n = min(n)
    else:
        n = sys.maxint
    return (sum([1 for nbr in range(0, 10) if sieve[transform_number(number, positions, nbr)]]), n)


def primes_count(number):
    number = str(number)
    return number_primes(number, 0, [])

def number_primes(number, pos, positions):
    if pos > len(number):
        return 0
    else:
        m = max(number_of_primes(number, positions), number_of_primes(number, positions+[pos]))
        m = max(m, number_primes(number, pos+1, positions), number_primes(number, pos+1, positions+[pos]))
        return m

def cnt(p):
    p = str(p)
    res = [number_of_primes(p, comb) for i in range(1, len(p)) for comb in itertools.combinations(range(1,len(p)-1), i)]
    if not res:
        return (0, sys.maxint)
    return (max([r[0] for r in res]), min([r[1] for r in res]))

cache = {}
found = True
for p in primes:
    print p
    (res, n) = cnt(p)
    if res == 8:
        print res
        print n
        break
    """
    if primes_count(p) == 8:
        print p
        break
    """

print cnt(120383)
