#!/usr/bin/python

import sys
import math

from project_euler import timeit


def is_triangle(a, b, c, perim):
    return a + b + c == perim and ((a * a) + (b * b) == (c * c))


def right_triangles(n):
    max_so_far = -sys.maxint
    solution = None
    for perim in xrange(0, n + 1, 2):
        solutions = 0
        for a in range(2, perim / 3):
            if (perim * perim - 2 * perim * a) % (2 * (perim - a)) == 0:
                solutions += 1

        if solutions > max_so_far:
            max_so_far = solutions
            solution = perim

    return solution


timeit(right_triangles, 1000)
