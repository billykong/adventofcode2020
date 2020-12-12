#!/usr/bin/env python3
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

def solution(input):
    parsed_input = parse_input(input)

    next = 0
    history = {}
    repeated = False
    acc = 0
    while not repeated:
        history[next] = True
        step = parsed_input[next]
        if step["operation"] == "nop":
            next += 1
        elif step["operation"] == "acc":
            acc += step["argument"]
            next += 1
        elif step["operation"] == "jmp":
            next += step["argument"]

        repeated = next in history

    return acc

print(solution(input))

assert(solution(test_input) == 5)
