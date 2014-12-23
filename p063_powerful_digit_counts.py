#!/usr/bin/python

import math

n = 1
lower = 1
cnt = 0
while lower < 10:
    lower = int(math.ceil(math.pow(10, (n - 1.0) / n)))
    cnt += (10 - lower)
    n += 1

print cnt
