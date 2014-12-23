#!/usr/bin/python

import math

LOW = 2
HIGH = 100

numbers = set()

for a in range(LOW, HIGH + 1):
    prev = a
    for b in range(LOW, HIGH + 1):
        numbers.add(prev * a)
        prev = prev * a

print len(list(numbers))



