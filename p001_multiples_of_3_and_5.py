#!/usr/bin/python

from project_euler import timeit


def multiples_of_3_and_5():
    return sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])


def multiples_of_3_and_5_2():
    result = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            result += i

    return result


timeit(multiples_of_3_and_5)
timeit(multiples_of_3_and_5_2)
