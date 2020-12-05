#!/usr/bin/env python3
import input

def q1(array):
    count = 0
    for i in range(1, len(array)):
        y_line = array[i]
        x = i * 3 %len(y_line)
        if y_line[x] == "#":
            count += 1

    return count


print(q1(input.array))