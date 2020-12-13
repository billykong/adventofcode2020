#!/usr/bin/env python3
from input import input, test_input


def parse_input(input):
    return [int(num) for num in input.split()]

def solution(input, preamble):
    parsed_input = parse_input(input)
    reference = []
    for i, num in enumerate(parsed_input):
        reference.append([])
        for offset in range(1, min(preamble, i+1)):
            reference[i].append(num + parsed_input[i - offset])

        candidates = set()
        for offset in range(0, min(preamble, i)):
            tmp = preamble - offset
            candidates.update({*reference[i-offset][0:tmp]})

        if i >= preamble and num not in candidates:
            return num


print(solution(input, 25))

assert(solution(test_input, 5) == 127)