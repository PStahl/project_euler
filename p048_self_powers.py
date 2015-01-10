#!/usr/bin/python

import math

from project_euler import timeit


def self_powers(last):
    TEN = 10000000000

    series = 0

    for n in range(1, last + 1):
        p = 1
        for i in range(n):
            p *= n
            p %= TEN


        series += p
        series %= TEN

    return str(series)


timeit(self_powers, 1000)
