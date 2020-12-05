#!/usr/bin/env python3
from input import input


dict = {}
for entry in input:
    target = 2020 - entry
    if target in dict:
        print (entry * target)
        break
    else:
        dict[entry] = True
