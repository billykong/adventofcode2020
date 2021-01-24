#!/usr/bin/env python3
from functools import reduce

from input import input, test_input


def parse_input(input):
    return [int(x) for x in input.split()]

def get_gap(input):
    shifted = input[1:] + input[0:1]
    return [0] + [b - a for a, b in zip(input, shifted)][:-1]

def jumps(distance):
    count = [0] * len(distance)
    count[0] = 1
    for i in range(0, len(distance)):
        travelled = 0
        x = i
        while x > 0 and x > i - 3:
            travelled += distance[x]
            x -= 1
            if travelled <= 3:
                # if we can at most jump 3 distance
                # counting how may possible ways to get to index i
                count[i] += count[x]
            else:
                break

    return count[-1]



def solution(input):
    parsed_input = parse_input(input)
    parsed_input.sort()
    full_chain = [0] + parsed_input + [parsed_input[-1] + 3]
    gaps = get_gap(full_chain)
    return jumps(gaps)

    

print(solution(input))

assert(solution(test_input) == 19208)
