#!/usr/bin/env python3.14

# Refer to https://docs.python.org/3/whatsnew/3.14.html#pep-750-template-string-literals

name = "Alice"
age = 30
template = t"Hello, my name is {name} and I am {age} years old."
print(
    "".join(
        item if isinstance(item, str) else str(item.value)
        for item in template
    )
)
