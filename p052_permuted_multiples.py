#!/usr/bin/python

import math

from collections import Counter

from project_euler import timeit


def is_permuted_multiple(n, number_of_digits):
    digits = Counter(str(n))
    return all(digits == Counter(str(n*i)) for i in range(2, number_of_digits))



def permuted_multiples(number_of_digits):
    n = int(math.pow(10, number_of_digits - 1))
    while True:
        for i in range(n, n * 10 / number_of_digits):
            if is_permuted_multiple(i, number_of_digits):
                return i
        n *= 10


timeit(permuted_multiples, 6)
