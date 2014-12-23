#!/usr/bin/python

from project_euler import timeit


def special_pythagorean_triplet(n):
    for a in range(n / 3):
        for b in range(a, n / 2):
            c = n - a - b

            if a * a + b * b == c * c:
                return (a, b, c)

    return (0, 0, 0)


timeit(special_pythagorean_triplet, 1000)
