#!/usr/bin/python

from project_euler import timeit


def combinatoric_selections(lowest_n, highest_n, upper_limit):
    factors = [1, 1]
    for n in range(2, highest_n + 1):
        factors.append(n * factors[n-1])

    def c(n, r):
        return factors[n]/(factors[r] * factors[n-r])

    result = [1 for n in range(1, highest_n + 1) for r in range(1, n + 1) if c(n, r) > upper_limit]
    return len(result)


timeit(combinatoric_selections, 1, 100, 1000000)
