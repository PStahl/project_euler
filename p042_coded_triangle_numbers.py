#!/usr/bin/python

def term(n):
    return n * (n + 1) / 2

vals = {}
s = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for c in s:
    vals[c] = s.index(c) + 1

def word_value(w):
    return sum(map(lambda c: vals[c], w))

with open('p042_words.txt', 'r') as f:
    words = f.read().split(",")
    words = [w.strip('\"') for w in words]

    N = max([len(w) for w in words])
    triangular = [term(n) for n in range(1, 2*N)]
    print len([w for w in words if sum([vals[c] for c in w]) in triangular])

