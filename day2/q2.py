#!/usr/bin/env python3
from input import input

import re

count = 0
for line in input:
  result = re.search(r"^(\d+)-(\d+)\s(\w):\s(.*)$", line)
  first = int(result.group(1))
  second = int(result.group(2))
  char = result.group(3)
  password = result.group(4)
  is_in_first_place = (password[first - 1] == char)
  is_in_second_place = (password[second - 1] == char)

  if is_in_first_place and not is_in_second_place:
    count += 1
  elif not is_in_first_place and is_in_second_place:
    count += 1

print(count)
