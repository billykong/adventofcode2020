#!/usr/bin/env python3
import re

from input import input, test_input


# From
"""
abc

a
b
c

ab
ac

a
a
a
a

b
"""
# To [['abc'], ['a', 'b', 'c'], ['ab', 'ac'], ['a', 'a', 'a', 'a'], ['b']]
def parse_input(input):
    intermediate = input.split("\n\n")
    intermediate = [re.sub(r"^\n", "", group) for group in intermediate]
    intermediate = [re.sub(r"\n$", "", group) for group in intermediate]
    intermediate = [group.split("\n") for group in intermediate]
    return intermediate

def q2(input):
    input_array = parse_input(input)
    total = 0
    for group in input_array:
        choice_count_in_group = {}
        for person in group:
            for choice in person:
                if choice not in choice_count_in_group:
                    choice_count_in_group[choice] = 1
                else:
                    choice_count_in_group[choice] += 1
        
        for choice in choice_count_in_group:
            if choice_count_in_group[choice] == len(group):
                total += 1

    return total

print(q2(input))

assert(q2(test_input) == 6)