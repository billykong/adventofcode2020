#!/usr/bin/env python3
from input import input, test_input


def binary_partitioning(lower_key, upper_key, str):
    binary_str = str.replace(lower_key, "0").replace(upper_key, "1")
    return int(binary_str, 2)

def get_row_number(str):
    return binary_partitioning("F", "B", str)

def get_column_number(str):
    return binary_partitioning("L", "R", str)

def get_seat_id(str):
    row_number = get_row_number(str[0:7])
    column_number = get_column_number(str[7:10])
    return row_number * 8 + column_number

def q1(input):
    max_seat_id = 0
    for str in input:
        seat_id = get_seat_id(str)
        # print(seat_id)
        if seat_id > max_seat_id:
            max_seat_id = seat_id

    return max_seat_id


print(q1(input))

assert(q1(test_input) == 820)