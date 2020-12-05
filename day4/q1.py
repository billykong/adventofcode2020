#!/usr/bin/env python3

# from test_input import input
from input import input


REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def clear_input(input):
    intermediate = input.split("\n\n")
    intermediate = list(map(lambda a: a.replace("\n", " "), intermediate))
    intermediate = list(map(lambda a: a.split(" "), intermediate))
    result = []
    for key_value_array in intermediate:
        passport_dict = {}
        for key_value in key_value_array:
            if len(key_value) > 0:
                passport_dict[key_value.split(":")[0]] = key_value.split(":")[1]
        result.append(passport_dict)

    return result

def q1(input, required_fields=REQUIRED_FIELDS):
    input = clear_input(input)
    count = 0
    for passport in input:
        missed_key = False
        for key in required_fields:
            if key not in passport:
                missed_key = True
        if missed_key == False:
            count += 1

    return count


print(q1(input))