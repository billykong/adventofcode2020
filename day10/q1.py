#!/usr/bin/env python3
from input import input, test_input


def parse_input(input):
    return [int(x) for x in input.split()]

def gap_count(array, gap):
    count = 0
    prev = array[0]
    for cur in array[1:]:
        count += 1 if (cur - prev) == gap else 0
        prev = cur
    return count

def solution(input):
    parsed_input = parse_input(input)
    parsed_input.sort()
    full_chain = [0] + parsed_input + [parsed_input[-1] + 3]
    count_1_diff = gap_count(full_chain, 1)
    count_3_diff = gap_count(full_chain, 3)
    return count_1_diff * count_3_diff
    

print(solution(input))

assert(solution(test_input) == 220)