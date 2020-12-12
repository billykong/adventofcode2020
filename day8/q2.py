#!/usr/bin/env python3
from copy import deepcopy

from input import input, test_input

def parse_input(input):
    lines = input.split("\n")
    result = []
    for line in lines:
        (op, arg) = line.split()
        result.append({
            "operation": op,
            "argument": int(arg)
        })
    return result

def recursion_helper(parsed_input, next, history, acc, changed):
    if next in history:
        return None
    if next >= len(parsed_input) or next < 0:
        return acc

    history[next] = True

    step = parsed_input[next]
    if step["operation"] == "acc":
        acc += step["argument"]
        acc_next = next + 1
        return recursion_helper(parsed_input, acc_next, history, acc, changed)
    else:
        nop_next = next + 1
        jmp_next = next + step["argument"]
        if changed:
            if step["operation"] == "nop":
                return recursion_helper(parsed_input, nop_next, history, acc, changed)
            elif step["operation"] == "jmp":
                return recursion_helper(parsed_input, jmp_next, history, acc, changed)
        else:
            if step["operation"] == "nop":
                option_1 = recursion_helper(parsed_input, nop_next, deepcopy(history), acc, False)
                option_2 = recursion_helper(parsed_input, jmp_next, deepcopy(history), acc, True)
                return option_1 if option_1 is not None else option_2
            elif step["operation"] == "jmp":
                option_1 = recursion_helper(parsed_input, nop_next, deepcopy(history), acc, True)
                option_2 = recursion_helper(parsed_input, jmp_next, deepcopy(history), acc, False)
                return option_1 if option_1 is not None else option_2

def solution(input):
    parsed_input = parse_input(input)
    return recursion_helper(parsed_input, 0, {}, 0, False)

print(solution(input))

assert(solution(test_input) == 8)