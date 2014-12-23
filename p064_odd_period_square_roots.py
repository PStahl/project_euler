#!/usr/bin/python

def rational(den, num, n):
    if n == 0:
        return den
    else:
        return rational(2*num + den, num + den, n - 1)


#print sum([int(c) for c in list(str(rational(3, 2, 101)))])

n0, n1, L = 1, 2, 100

for i in range(2, L):
    n1, n0 = n0, n1 + n0 * (1 if i % 3 else 2 * i//3)
print L,"convergent for e =", sum(map(int, str(n0)))


