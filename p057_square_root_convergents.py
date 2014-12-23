#!/usr/bin/python

cache = {}

pell = [0, 1]
H = [1, 1]

res = 0
for n in range(2, 1001):
    pell.append(2*pell[n-1] + pell[n-2])
    H.append(H[n-1] + 2 * pell[n-1])
    if len(str(H[n])) > len(str(pell[n])):
        res += 1

print res

