#!/usr/bin/env python3
import input


def q2(array, x_step, y_step):
    count = 0
    for i in range(0, len(array), y_step):
        y_line = array[i]
        x = int(i / y_step) * x_step %len(y_line)
        if y_line[x] == "#":
            count += 1

    return count


x1y1 = q2(input.array, 1, 1); print(x1y1)
x3y1 = q2(input.array, 3, 1); print(x3y1)
x5y1 = q2(input.array, 5, 1); print(x5y1)
x7y1 = q2(input.array, 7, 1); print(x7y1)
x1y2 = q2(input.array, 1, 2); print(x1y2)

print(x1y1 * x3y1 * x5y1 * x7y1 * x1y2)