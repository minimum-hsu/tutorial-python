#!/usr/bin/env python3

# Using underscore as a throwaway variable in a loop
for _ in range(3):
    print("_", end="")

# Using underscore to ignore specific values during unpacking
one, _, three = [1, 2, 3]
print("\nFirst:", one)
print("Third:", three)