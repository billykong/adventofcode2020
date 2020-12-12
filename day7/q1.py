#!/usr/bin/env python3
import re

from input import input, test_input


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
            color = re.match(r"(\d+)\s(.*?)\sbag", substr).group(2)
            count = re.match(r"(\d+)\s(.*?)\sbag", substr).group(1)
            contain_colors[color] = count
        result[key] = contain_colors
    return result

def recursion_helper(color_dict, current_color, target_color, history={}):
    if current_color in  history:
        return False
    else:
        history[current_color] = True

    children_colors = color_dict[current_color]
    result = False
    for color in children_colors:
        if target_color == color:
            return True
        else:
            result = result or recursion_helper(color_dict, color, target_color, history)
    return result

def solution(input):
    color_dict = parse_input(input)
    count = 0
    for color in color_dict:
        count += recursion_helper(color_dict, color, "shiny gold", {})
    return count


print(solution(input))

assert(solution(test_input) == 4)