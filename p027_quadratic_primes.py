#!/usr/bin/python


sieve = [True] * 1000000 # Sieve is faster for 2M primes
def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]: mark(sieve, x)


def f(a, b, n):
    return n * n + a * n + b


LOWER_LIMIT = -1000
UPPER_LIMIT = 1000

m = 0
a_and_b = (0, 0)
a = LOWER_LIMIT + 1
while a < UPPER_LIMIT:
    b = LOWER_LIMIT + 1
    while b < UPPER_LIMIT:
        n = 0
        while sieve[f(a, b, n)]:
            n += 1
        if n > m:
            m = n
            a_and_b = (a, b)
        b += 1
    a += 1

print m
print a_and_b
print a_and_b[0] * a_and_b[1]




