#!/usr/bin/python

from project_euler import timeit

coins = (200, 100, 50, 20, 10, 5, 2, 1)
cache = {}


def combinations(total, coins):
    if total == 0:
        return 1
    elif total < 0 or not coins:
        return 0
    elif (total, coins) in cache:
        return cache[(total, coins)]

    n = 0
    for c in coins:
        n += combinations(total - c, filter(lambda x: x <= c, coins))

    cache[(total, coins)] = n
    return n


timeit(combinations, 200, coins)
