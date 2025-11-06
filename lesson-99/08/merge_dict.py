#!/usr/bin/env python3

map_a = {'a': 1, 'b': 2}
map_b = {'b': 3, 'c': 4}

# Merging two dictionaries using the unpacking operator **
merged_map = {**map_a, **map_b}
print("Merged Dictionary:", merged_map)

# Merging two dictionaries using the update() method
merged_map = map_a.copy()  # Create a copy to avoid modifying the original
merged_map.update(map_b)
print("Merged Dictionary using update():", merged_map)

# Merging two dictionaries using the | operator (Python 3.9+)
merged_map = map_a | map_b
print("Merged Dictionary using | operator:", merged_map)