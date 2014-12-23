#!/usr/bin/python

from collections import Counter

UPPER_LIMIT = 9999 # 1 x 9999 = 9999 == 9 digits

DIGITS = Counter("123456789")

def is_unusual(a, b, c):
    s = str(a) + str(b) + str(c)
    if len(s) > 9:
        return False

    return DIGITS == Counter(s)

unusual = set()
for i in range(1, 100):
    for j in range(1, 10000):
        if any(c in str(j) for c in str(i)):
            continue
        if is_unusual(i, j, i * j):
            unusual.add(i * j)

print sum(list(unusual))

