#!/usr/bin/python2.7

from project_euler import timeit


def number_of_paths(n, cache=None, pos_x=0, pos_y=0):
    if not cache:
        cache = [[-1 for i in range(n)] for j in range(n)]
        cache[n - 1][n - 1] = 1

    if pos_x >= n or pos_y >= n:
        return 0
    elif cache[pos_x][pos_y] > 0:
        return cache[pos_x][pos_y]
    else:
        cache[pos_x][pos_y] = number_of_paths(n, cache, pos_x + 1, pos_y) + number_of_paths(n, cache, pos_x, pos_y + 1)
        return cache[pos_x][pos_y]


timeit(number_of_paths, 21)
