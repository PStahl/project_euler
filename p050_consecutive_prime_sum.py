#!/usr/bin/python

N = 1000000

def is_prime(n):
    if any(n % p == 0 for p in primes):
        return True
    else:
        return False

sieve = [True] * 2*N
def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]: mark(sieve, x)

primes = [i for i in xrange(2, len(sieve)) if sieve[i]]

m = 0
max_prime = 0
for i in range(N):
    if primes[i] > N:
        break

    j = 1
    s = sum(primes[i:i+j])
    while s < N and j < N:
        if sieve[s] and j > m:
            m = j
            max_prime = s

        j += 1
        s = sum(primes[i:i+j])




print m
print max_prime
