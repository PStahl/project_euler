#!/usr/bin/python

import math
import bisect
from itertools import permutations
from collections import defaultdict

def largest_permutation(n):
    numbers = reversed(sorted(list(str(n))))
    max_n = 0
    for n in numbers:
        max_n = max_n * 10 + int(n)

    return max_n

cubes = []
cache = defaultdict(int)
smallest = {}

n = 345
done = False
while not done:
    n += 1
    largest = largest_permutation(long(math.pow(n, 3)))
    if not largest in cubes:
        bisect.insort(cubes, largest)

    if not largest in smallest:
        smallest[largest] = n

    cache[largest] += 1
    if cache[largest] == 5:
        print long(math.pow(smallest[largest], 3))
        break



