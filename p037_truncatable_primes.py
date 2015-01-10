#!/usr/bin/python


from project_euler import timeit, sieves


def is_truncatable(sieve, n):
    if len(str(n)) == 1:
        return sieve[n]
    else:
        return (sieve[n] and
                all(sieve[int(str(n)[i:])] and
                    sieve[int(str(n)[0:-i])] for i in range(1, len(str(n)))))


def truncatable_primes(n):
    sieve = sieves(n)
    sieve[1] = False

    res = []
    i = 11
    while len(res) < 11:
        if is_truncatable(sieve, i):
            res.append(i)
        i += 1

    return sum(res)


timeit(truncatable_primes, 10000000)
