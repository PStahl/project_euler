#!/usr/bin/python

from project_euler import timeit


def triangle(n):
    return n * (n + 1) / 2


def pentagonal(n):
    return n * (3 * n - 1) / 2


def hexagonal(n):
    return n * (2 * n - 1)


def triang_penta_hexa_number(start_t, start_p, start_h):
    t = start_t
    p = start_p
    h = start_h
    found = False
    while not found:
        triang = triangle(t)
        while triang < max(pentagonal(p), hexagonal(h)):
            triang = triangle(t)
            t += 1

        while pentagonal(p) < triang:
            p += 1

        while hexagonal(h) < triang:
            h += 1

        if triang == pentagonal(p) and triang == hexagonal(h):
            found = True
            return triang 


timeit(triang_penta_hexa_number, 286, 165, 143)
