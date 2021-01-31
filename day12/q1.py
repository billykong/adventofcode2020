#!/usr/bin/env python3

from input import input, test_input

DIRECTIONS = ('E', 'S', 'W', 'N')
CLOCKWISE = { 'L': -1, 'R': 1 }

def parse_input(input):
    return input

def update_direction(instruction, direction):
    (clockwise, degree) = (CLOCKWISE[instruction[0]], int(instruction[1:]))
    quarters = (clockwise * degree) // 90
    return DIRECTIONS[(DIRECTIONS.index(direction) + quarters) % 4]

def get_forward_backward(sail_to, direction, course):
    if sail_to in course:
        return 1 if sail_to == course[0] else -1
    elif sail_to == 'F' and direction in course:
        return 1 if direction == course[0] else -1
    else:
        return 0

def get_east_west_adjustment(instruction, direction):
    distance = int(instruction[1:])
    return get_forward_backward(instruction[0], direction, ('E', 'W')) * distance

def get_north_south_adjustment(instruction, direction):
    distance = int(instruction[1:])
    return get_forward_backward(instruction[0], direction, ('N', 'S')) * distance

def solution(input):
    input = parse_input(input)
    direction = 'E'
    east_west, north_south = (0, 0)
    for instruction in input:
        if instruction[0] in ('L', 'R'):
            direction = update_direction(instruction, direction)
        else:
            east_west += get_east_west_adjustment(instruction, direction)
            north_south += get_north_south_adjustment(instruction, direction)
    return abs(east_west) + abs(north_south)

#print(solution(test_input))
print(solution(input))

#assert(solution(test_input) == 17)
