#!/usr/bin/env python3

array_a = [1, 2, 3]
array_b = [4, 5, 6]

# Merging two lists using the + operator
merged_array = array_a + array_b
print("Merged List using + operator:", merged_array)

# Merging two lists using unpacking operator *
merged_array = [*array_a, *array_b]
print("Merged List using unpacking * operator:", merged_array)

# Merging two lists using extend() method
merged_array = array_a.copy()  # Create a copy to avoid modifying the original
merged_array.extend(array_b)
print("Merged List using extend() method:", merged_array)

# Merging two lists using itertools.chain
import itertools
merged_array = list(itertools.chain(array_a, array_b))
print("Merged List using itertools.chain:", merged_array)