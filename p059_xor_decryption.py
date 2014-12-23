#!/usr/bin/python

values = open("p059_cipher.txt", "r").read().split(",")

for i in range(100, 1000):
    start = 0
    end = 0
    so_far = []
    while end < len(values):
        end += 1
        so_far.append(values[end])
        if is_a_word(so_far, start, end):
            start = end + 1
            end = start
            so_far = []




