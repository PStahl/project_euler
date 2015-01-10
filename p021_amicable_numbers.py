#!/usr/bin/python

from collections import defaultdict

from project_euler import timeit

cache = {}


def sum_divisors(n):
    if n in cache:
        return cache[n]

    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i

    cache[n] = s
    return s


def amicable_pairs_xrange(low, high):
    L = [sum_divisors(i) for i in range(low, high + 1)]
    result = 0
    for i in range(high - low + 1):
        ind = L[i]
        if i + low < ind and low <= ind and ind <= high and L[ind - low] == i + low:
            result += i + low + ind
    
    return result


timeit(amicable_pairs_xrange, 1, 10000)
