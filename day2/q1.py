#!/usr/bin/env python3
from input import input

import re

count = 0
for line in input:
  result = re.search(r"^(\d+)-(\d+)\s(\w):\s(.*)$", line)
  min = int(result.group(1))
  max = int(result.group(2))
  char = result.group(3)
  password = result.group(4)
  char_count = password.count(char)
  if char_count >= min and char_count <= max:
    count += 1

print(count)
