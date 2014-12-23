#!/usr/bin/python2.7

N = 100


factorial = 1
n = 2

while n <= N:
    factorial *= n
    if factorial % 10 == 0:
        factorial = factorial / 10
    n += 1

nbrs = map(lambda x: int(x), str(factorial))
print sum(nbrs)
