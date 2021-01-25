#!/usr/bin/env python3

from input import input, test_input

TOLERANCE = 5

def parse_input(input):
    return [list(row) for row in input]

def is_taken(seat):
    return seat == '#'

def is_empty(seat):
    return seat == 'L'

def empty(row, column, seats):
    seats[row][column] = 'L'

def sit(row, column, seats):
    seats[row][column] = '#'

def is_first_seat_occupied(row, column, seats, row_offset, column_offset):
    next_row = row + row_offset
    next_column = column + column_offset
    if next_row >= 0 and next_row < len(seats) and next_column >= 0 and next_column < len(seats[0]):
        seat = seats[next_row][next_column]
        if is_empty(seat):
            return False
        else:
            return is_taken(seat) or is_first_seat_occupied(next_row, next_column, seats, row_offset, column_offset)
    else:
        return False

def surround_taken_count(row, column, seats):
    count = 0
    
    directions = ((r, c) for r in (1, 0, -1) for c in (1, 0, -1))
    for direction in directions:
        if is_first_seat_occupied(row, column, seats, direction[0], direction[1]):
            count += 1
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
            if surround_taken_count(row, column, seats) >= TOLERANCE:
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

# print(solution(test_input))
print(solution(input))

assert(solution(test_input) == 26)

