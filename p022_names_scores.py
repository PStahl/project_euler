#!/usr/bin/python


def to_value_string(name):
    return [ord(c) - ord('A') + 1 for c in name]

def to_position_score(name_score, pos):
    return sum(name_score) * pos

f = open('p022_names.txt', 'r')
names = sorted(map(lambda name: to_value_string(name.replace("\"", "")), f.read().split(",")))
f.close()

for i in range(len(names)):
    names[i] = to_position_score(names[i], i + 1)

print sum(names)
