#!/usr/bin/python


sieve = [True] * 10000000 # Sieve is faster for 2M primes
def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]: mark(sieve, x)

sieve[1] = False

def is_truncatable(n):
    if len(str(n)) == 1:
        return sieve[n]
    else:
        return (sieve[n] and
                all(sieve[int(str(n)[i:])] and sieve[int(str(n)[0:-i])] for i in range(1, len(str(n)))))


res = []
i = 11
while len(res) < 11:
    if is_truncatable(i):
        res.append(i)
    i += 1

print res
print len(res)
print sum(res)
"""
for n in res:
    print n
    print [str(n)[i:] for i in range(1, len(str(n)))]
    print [str(n)[0:-i] for i in range(1, len(str(n)))]
"""
