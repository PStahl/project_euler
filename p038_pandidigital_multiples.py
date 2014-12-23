#!/usr/bin/python

from collections import Counter

UPPER_LIMIT = 99999

DIGITS = Counter("123456789")

def concatenated(l):
    return reduce(lambda x, y: str(x) + str(y), l)

def is_pandigital(s):
    if len(s) > 9:
        return False

    return DIGITS == Counter(s)

m = 0

for i in range(1, UPPER_LIMIT):
    t = [1, 2]
    s = concatenated(map(lambda x: x * i, t))
    while len(s) < 10:
        if is_pandigital(s):
            if int(s) > m:
                m = int(s)
        t.append(t[-1] + 1)
        s = concatenated(map(lambda x: x * i, t))

print m
