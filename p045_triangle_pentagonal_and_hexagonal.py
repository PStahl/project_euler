#!/usr/bin/python

def triangle(n):
    return n * (n + 1) / 2

def pentagonal(n):
    return n * (3 * n - 1) / 2

def hexagonal(n):
    return n * (2 * n - 1)

t = 285 + 1
p = 165
h = 143
found = False
while not found:
    T = triangle(t)
    while T < max(pentagonal(p), hexagonal(h)):
        T = triangle(t)
        t += 1

    while pentagonal(p) < T:
        p += 1
    while hexagonal(h) < T:
        h += 1

    if T == pentagonal(p) and T == hexagonal(h):
        found = True
        print T
