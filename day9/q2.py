#!/usr/bin/env python3
from input import input, test_input


def parse_input(input):
    # is it possible to make it lazy and subscriptable?
    return [int(num) for num in input.split()] 

def solution(input, target):
    parsed_input = parse_input(input)
    (first_i, last_i) = (0, 1)
    current_sum = parsed_input[first_i] + parsed_input[last_i]
    while last_i < len(parsed_input):
        if current_sum < target:
            last_i += 1
            current_sum += parsed_input[last_i]
        elif current_sum > target:
            current_sum -= parsed_input[first_i]
            first_i += 1
        else:
            max_num = max(parsed_input[first_i:last_i+1])
            min_num = min(parsed_input[first_i:last_i+1])
            return max_num + min_num



print(solution(input, 29221323))

assert(solution(test_input, 127) == 62)
