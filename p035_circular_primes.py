#!/usr/bin/python

def nbrs(i):
    s = str(i)
    nbrs = []
    for i in range(len(s)):
        nbrs.append(int(s[i:] + s[0:i]))
    return nbrs

def is_circular(i):
    return all(sieve[n] for n in nbrs(i))

sieve = [True] * 1000000 # Sieve is faster for 2M primes
def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]: mark(sieve, x)

primes = [i for i in xrange(2, len(sieve)) if sieve[i] and is_circular(i)]

print len(primes)
