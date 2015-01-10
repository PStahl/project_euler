#!/usr/bin/python

from project_euler import timeit


def name_scores():
    f = open('p022_names.txt', 'r')
    values = sorted(map(lambda name: to_string_value(name.replace("\"", "")), f.read().split(",")))
    f.close()

    result = 0
    for index, character_values in enumerate(values):
        result += sum(character_values) * (index + 1)

    return result


def to_string_value(name):
    return [ord(c) - ord('A') + 1 for c in name]


timeit(name_scores)
