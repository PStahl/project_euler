#!/usr/bin/python

UPPER_LIMIT = 1000000

n = 0
i = 1
current = 1
result = []

while n <= UPPER_LIMIT:
    s = str(i)
    if n % current == 0:
        result.append(i)
        current = current * 10
    elif (n + len(str(i))) % current < len(str(i)):
        s = str(i)
        while not n % current == 0:
            n += 1
            c = int(s[0])
            s = s[1:]
        result.append(c)
        current = current * 10

    n += len(s)
    i += 1

print reduce(lambda x, y: x * y, result)
