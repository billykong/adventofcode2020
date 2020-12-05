#!/usr/bin/env python3
from input import input


def q2(input, x_step, y_step):
    count = 0
    for i in range(0, len(input), y_step):
        y_line = input[i]
        x = int(i / y_step) * x_step %len(y_line)
        if y_line[x] == "#":
            count += 1

    return count


x1y1 = q2(input, 1, 1)
x3y1 = q2(input, 3, 1)
x5y1 = q2(input, 5, 1)
x7y1 = q2(input, 7, 1)
x1y2 = q2(input, 1, 2)

print(x1y1 * x3y1 * x5y1 * x7y1 * x1y2)