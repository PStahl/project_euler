#!/usr/bin/python

from collections import Counter
import math

def is_permuted(n):
    digits = Counter([c for c in list(str(n))])
    return all(Counter(digits) == Counter(list(str(n*i))) for i in range(2, 7))

n = 1
found = False
while not found:
    n *= 10
    for i in range(n, n*10/6):
        if is_permuted(i):
            print i
            found = True
            break
