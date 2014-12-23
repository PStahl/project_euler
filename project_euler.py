#!/usr/bin/python

import time


def timeit(fun, *args):
    start = time.time()
    result = fun(*args)
    end = time.time()
    print "Result: {}".format(result)
    print "Time: {} ms".format(1000 * (end - start))


def sieves(n):
    sieve = [True] * n 

    for x in xrange(2, int(len(sieve) ** 0.5) + 1):
        if sieve[x]:
            for i in xrange(x+x, len(sieve), x):
                sieve[i] = False

    return sieve



def get_n_primes(n, init=1000000):
    sieve = sieves(init)
    return [p for p in xrange(2, len(sieve)) if sieve[p]][:n]



def prime_factorisation_no(n, primes=None):
    if not primes:
        primes = get_primes_under_n(n)

    nod = 1
    exponent = 1
    remain = n

    for p in primes:
        if p * p > n:
            return nod * 2

        exponent = 1
        while remain % p == 0:
            exponent += 1
            remain = remain / p

        nod *= exponent

        if remain == 1:
            return nod
    
    return nod


def get_primes_under_n(n):
    if n > 100000:
        return [p for p in get_n_primes(n) if p < n]
    
    primes = [2]
    is_prime = False
    
    for i in range(3, n + 1):
        j = 0
        is_prime = True
        while (primes[j] * primes[j] <= i):
            if i % primes[j] == 0:
                is_prime = False
                break
            j += 1
        if is_prime:
            primes.append(i)
    return primes


def get_nth_prime(n):
    return get_n_primes(n)[-1]


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_palindrome_2(n):
    s = str(n)
    return all(s[i] == s[len(s) - 1 - i] for i in range(0, (len(s) / 2)))




