#!/usr/bin/python

import math

TEN = 10000000000

series = 0

for n in range(1, 1001):
    p = 1
    for i in range(n):
        p *= n
        p %= TEN


    series += p
    series %= TEN

print str(series)


