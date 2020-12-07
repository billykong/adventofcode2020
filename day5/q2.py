#!/usr/bin/env python3
from input import input, test_input

def binary_partitioning(lower_key, upper_key, str):
    binary_str = str.replace(lower_key, "0").replace(upper_key, "1")
    return int(binary_str, 2)

def get_row_number(str):
    return binary_partitioning("F", "B", str)

def get_column_number(str):
    return binary_partitioning("L", "R", str)

def q2(input):
    seat_plan = {}
    for str in input:
        row_number = get_row_number(str[0:7])
        column_number = get_column_number(str[7:10])
        if row_number not in seat_plan:
            seat_plan[row_number] = []
        seat_plan[row_number].append(column_number)
    for row_number in seat_plan:
        row = seat_plan[row_number]
        if len(row) == 7: # exactly one seat not taken
            row.sort()
            for i in range(0, len(row)):
                if i != row[i]:
                    return row_number * 8 + i
    
print(q2(input))