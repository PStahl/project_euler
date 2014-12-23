#!/usr/bin/python

coins = [200, 100, 50, 20, 10, 5, 2, 1]

N = 200

cache = [0 for i in range(0, N + 1)]

def combinations(total, coins):
    if total == 0:
        return 1
    elif total < 0 or not coins or len(coins) < 1:
        return 0

    n = 0
    for c in coins:
        #print c
        n += combinations(total - c, filter(lambda x: x <= c, coins))

    cache[total] = n
    return n

print combinations(200, coins)




