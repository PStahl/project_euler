#!/usr/bin/python

sieve = [True] * 2000000 # Sieve is faster for 2M primes
def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]: mark(sieve, x)

def is_prime(n):
    if n < len(sieve):
        return sieve[n]

    if (n <= 1):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    if (n < 9):
        return True
    if (n % 3 == 0):
        return False

    counter = 5;
    while ((counter * counter) <= n):
        if (n % counter == 0):
            return False
        if (n % (counter + 2) == 0):
            return False
        counter += 6;

    return True;


def corner_numbers(n):
    last = (n * 2 + 1) ** 2
    return [last - i*2*(n) for i in range(4)]

ratio = 100
layer = 1
primes = 0.0
total = 1
while 100 * ratio > 10:
    new_numbers = corner_numbers(layer)
    layer += 1
    for nbr in new_numbers:
        if is_prime(nbr):
            primes += 1
    total += 4
    ratio = primes / total

print (layer-1) * 2 + 1
