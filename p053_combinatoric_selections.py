#!/usr/bin/python

factors = [1, 1]
for n in range(2, 101):
    factors.append(n * factors[n-1])

def c(n, r):
    return factors[n]/(factors[r] * factors[n-r])

N = 1000000

result = [1 for n in range(1, 101) for r in range(1, n+1) if c(n, r) > N]
print len(result)
