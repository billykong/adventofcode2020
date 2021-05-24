#!/usr/bin/env python3

from input import test_input, input


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a, b):
    return int((a * b)/gcd(a, b))

def next_departure_for_route(start_at, route):
    for step in range(route):
        if (start_at + step) % route == 0:
            return start_at + step

def solution(input):
    route_list = [x if x == 'x' else int(x) for x in input.routes.split(',')]

    step = int(route_list[0])
    start_at = next_departure_for_route(input.timestamp, step)
    for route in route_list[1:]:
        start_at += 1
        if route == 'x':
            continue
        while (start_at % route) != 0:
            start_at += step

        step = lcm(step, route)
    return start_at - len(route_list) + 1


if __name__ == "__main__":
    print(solution(test_input))
    print(solution(input))
