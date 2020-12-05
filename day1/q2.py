#!/usr/bin/env python3
from input import input


input.sort()
for i, current in enumerate(input):
    left = i
    right = len(input) - 1
    while left < right:
        sum = (current + input[left] + input[right])
        if sum == 2020:
            print (current * input[left] * input[right])
            break
        elif sum < 2020:
            left += 1
        else:
            right -= 1

