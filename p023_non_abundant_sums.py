#!/usr/bin/python

from project_euler import timeit, divisors

import math


def sum_of_non_abundant(n):
    abundants = set([i for i in range(1, n) if is_abundant(i)])

    return sum([i for i in range(1, n + 1) if not is_abundant_sum(abundants, i)])


def is_abundant(n):
    if n < 12:
        return False
    return sum(divisors(n)) > n


def is_abundant_sum(abundants, n):
   for i in abundants:
       if i > n:  # assume "abundants" is ordered
         return False
       if (n - i) in abundants:
           return True
   return False


timeit(sum_of_non_abundant, 28123)
