#!/usr/bin/env python3
import re
import sys

from test_input import input_valid, input_invalid
from input import input


REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def clear_input(input):
    intermediate = input.split("\n\n")
    intermediate = map(lambda a: a.split(), intermediate)
    result = []
    for key_value_array in intermediate:
        passport_dict = {}
        for key_value in key_value_array:
            if len(key_value) > 0:
                passport_dict[key_value.split(":")[0]] = key_value.split(":")[1]
        result.append(passport_dict)

    return result

def validate_year(key, start_year, end_year, passport):
    if key not in passport:
        return False

    value = passport[key]
    if not re.match(r"\d{4}$", value):
        return False

    if int(value) < start_year or int(value) > end_year:
        return False

    return True

def validate_byr(passport):
    return validate_year("byr", 1920, 2002, passport)

def validate_iyr(passport):
    return validate_year("iyr", 2010, 2020, passport)

def validate_eyr(passport):
    return validate_year("eyr", 2020, 2030, passport)

def validate_hgt(passport):
    if "hgt" not in passport:
        return False

    match = re.match(r"(\d{2,3})(cm|in)", passport["hgt"])
    if not match:
        return False

    value = int(match[1])
    unit = match[2]
    
    if unit == "cm" and (value < 150 or value > 193):
        return False

    if unit == "in" and (value < 59 or value > 76):
        return False

    return True


def validate_regex(key, regex, passport):
    if key not in passport:
        return False

    if not re.match(regex, passport[key]):
        return False

    return True


def validate_hcl(passport):
    return validate_regex("hcl", r"^#([a-f]|[0-9]){6}$", passport)


def validate_ecl(passport):
    return validate_regex("ecl", r"^(amb|blu|brn|gry|grn|hzl|oth)$", passport)


def validate_pid(passport):
    return validate_regex("pid", r"^(\d{9})$", passport)


def q2(input, required_fields=REQUIRED_FIELDS):
    input = clear_input(input)
    count = 0
    for passport in input:
        valid = True
        # go through each validation here
        for key in required_fields:
            valid = valid and getattr(sys.modules[__name__], "validate_{}".format(key))(passport)

        if valid == True:
            count += 1

    return count


print(q2(input))

assert(q2(input_valid) == 4)
assert(q2(input_invalid) == 0)
