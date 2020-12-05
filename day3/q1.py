#!/usr/bin/env python3
from input import input


def q1(input):
    count = 0
    for i in range(1, len(input)):
        y_line = input[i]
        x = i * 3 %len(y_line)
        if y_line[x] == "#":
            count += 1

    return count


print(q1(input))