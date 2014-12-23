#!/usr/bin/python

import math

def f(a, b, c, p):
    return a + b + c == p and ((a * a) + (b * b) == (c*c))


m = 0
m_p = 0
for p in xrange(0, 1001, 2):
    n = 0
    for a in range(2, p / 3):
        if (p*p-2*p*a) % (2*(p-a)) == 0:
            n += 1

    if n > m:
        m = n
        m_p = p

print m
print m_p

