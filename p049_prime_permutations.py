#!/usr/bin/python

from itertools import permutations

def is_prime(n):
    if any(n % p == 0 for p in primes):
        return True
    else:
        return False

sieve = [True] * 10000 # Sieve is faster for 2M primes
def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]: mark(sieve, x)

primes = [i for i in xrange(2, len(sieve)) if sieve[i] and len(str(i)) == 4]

def to_digit(n):
    return int(reduce(lambda x,y: x + y, n))

for prime in primes:
    prime_perms = []
    for perm in filter(lambda x: x >= 1000, map(to_digit, list(permutations(str(prime), 4)))):
        if sieve[perm]:
            prime_perms.append(perm)

    prime_perms = sorted(list(set(prime_perms)))
    if len(prime_perms) >= 3:
        result = []
        prev_diff = prime_perms[1] - prime_perms[0]
        result.append(prime_perms[0])
        result.append(prime_perms[1])
        i = 2
        while i < len(prime_perms):
            diff = prime_perms[i] - prime_perms[i - 1]
            if diff == prev_diff:
                result.append(prime_perms[i])
            else:
                result = [prime_perms[i-1], prime_perms[i]]

            if len(result) == 3:
                print result
                break

            i += 1

            prev_diff = diff

