#!/usr/bin/env python3

from input import test_input, input


def solution(input):
    route_list = input.routes.split(',')
    last_bus_gone_for = ((input.timestamp % int(route), int(route)) for route in route_list if route != 'x')
    min_wait = input.timestamp # or some very large number
    min_wait_route = 0
    for (gone_for, route) in last_bus_gone_for:
        wait = route - gone_for
        if wait < min_wait:
            min_wait = wait
            min_wait_route = route
   
    return min_wait * min_wait_route


if __name__ == "__main__":
    print(solution(test_input))
    print(solution(input))
