#!/usr/bin/env python3
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
# To ['abc', 'abc', 'abac', 'aaaa', 'b']
def parse_input(input):
    intermediate = input.split("\n\n")
    intermediate = [group.replace("\n","") for group in intermediate]
    return intermediate

def q1(input):
    input_str = parse_input(input)
    input_dict_array = []
    for str in input_str:
        dict = {}
        for char in str:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
        input_dict_array.append(dict)

    result = 0
    for dict in input_dict_array:
        result += len(dict)

    return result


print(q1(input))

assert(q1(test_input) == 11)