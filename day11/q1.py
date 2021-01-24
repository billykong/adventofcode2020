#!/usr/bin/env python3

from input import input, test_input
from itertools import product


def parse_input(input):
    return [list(row) for row in input]

def is_taken(seat):
    return seat == "#"

def is_empty(seat):
    return seat == "L"

def empty(row, column, seats):
    seats[row][column] = "L"

def sit(row, column, seats):
    seats[row][column] = "#"

def surround_taken_count(row, column, seats):
    count = 0
    for r in seats[max(row-1, 0): row+2]:
        count += len([c for c in r[max(column-1, 0): column+2] if is_taken(c)])
    
    if is_taken(seats[row][column]):
        count -= 1

    return count
    
def iterate_seats(width, height, seats):
    changed = False
    new_seats = [row[:] for row in seats] 
    indices = ((row, column) for row in range(height) for column in range(width))
    for row, column in indices:
        seat = seats[row][column]
        if is_taken(seat):
            if surround_taken_count(row, column, seats) >= 4:
                empty(row, column, new_seats)
                changed = True

        elif is_empty(seat):
            if surround_taken_count(row, column, seats) == 0:
                sit(row, column, new_seats)
                changed = True

    return (changed, new_seats)

def count_taken(seats):
    count = 0
    for row in seats:
        count += len([x for x in row if x == '#'])
    return count

def solution(input):
    seats = parse_input(input)
    width = len(seats[0])
    height = len(seats)
    while(True):
        changed, seats = iterate_seats(width, height, seats)
        if not changed:
            break
    return count_taken(seats)

print(solution(test_input))
# print(solution(input))

assert(solution(test_input) == 37)

