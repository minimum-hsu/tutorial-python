#!/usr/bin/env python3

list_comprehension = [x * 2 for x in range(10)]
dict_comprehension = {x: x * 2 for x in range(10)}
set_comprehension = {x * 2 for x in range(10)}
generator_comprehension = (x * 2 for x in range(10))

print("List Comprehension:", list_comprehension)
print("Dict Comprehension:", dict_comprehension)
print("Set Comprehension:", set_comprehension)
print("Generator Comprehension:", generator_comprehension, list(generator_comprehension))
