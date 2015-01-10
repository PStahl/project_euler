#!/usr/bin/python

from project_euler import timeit


def powerful_digit_sum(upper_limit):
    return max([sum([int(x) for x in str(a**b)]) for a in range(1, upper_limit) for b in range(1, 100)])


timeit(powerful_digit_sum, 100)


