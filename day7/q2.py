#!/usr/bin/env python3
import re

from input import input, test_input, test_input_2


"""
From 
light red bags contain 1 bright white bag, 2 muted yellow bags.
...

To 
{ 
    "light red": { 
        "bright white": 1,
        "muted yellow": 2
    },
    ...
}
"""
def parse_input(input):
    intermediate = input.split("\n")
    result = {}
    for line in intermediate:
        (key, value_str) = line.split(" bags contain ")
        contain_colors = {}
        for substr in value_str.split(", "):
            if "no other bags" in substr:
                break
            colour = re.match(r"(\d+)\s(.*?)\sbag", substr).group(2)
            count = int(re.match(r"(\d+)\s(.*?)\sbag", substr).group(1))
            contain_colors[colour] = count
        result[key] = contain_colors
    return result

def recursion_helper(color_dict, target_color):
    if len(color_dict[target_color]) == 0:
        return 0
    count = 0
    for color in color_dict[target_color]:
        color_count = color_dict[target_color][color]
        count += color_count
        count += color_count * recursion_helper(color_dict, color)

    return count

def solution(input):
    color_dict = parse_input(input)
    result = recursion_helper(color_dict, 'shiny gold')
    return result


print(solution(input))

assert(solution(test_input_2) == 126)