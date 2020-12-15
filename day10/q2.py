#!/usr/bin/env python3
from input import input, test_input, test_input_2


def parse_input(input):
    return [int(x) for x in input.split()]

def recursion_helper(array, count):
    if not array:
        return count

    current = array[0]
    if len(array) >= 2:
        count = recursion_helper(array[1:], count)
    if len(array) >= 3 and (array[2] - current) <= 3:
        count += 1
        count = recursion_helper(array[2:], count)
    if len(array) >= 4 and (array[3] - current) <= 3:
        count += 1
        count = recursion_helper(array[3:], count)

    return count

def solution(input):
    parsed_input = parse_input(input)
    parsed_input.sort()
    full_chain = [0] + parsed_input + [parsed_input[-1] + 3]
    return recursion_helper(full_chain, 1)

    

print(solution(input))

# assert(solution(test_input) == 19208)