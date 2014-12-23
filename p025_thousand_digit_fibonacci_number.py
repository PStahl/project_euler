#!/usr/bin/python

N = 1000

fibs = [1, 1, 2]
i = 2
while len(str(fibs[i])) < N:
    i += 1
    fibs.append(fibs[i - 1] + fibs[i - 2])

print i + 1
