#!/usr/bin/env python3

def iter_squares(n: int):
    array = [i * i for i in range(n)]
    yield from array

if __name__ == "__main__":
    print("Using iter_squares with yield from:")
    for square in iter_squares(10):
        print(square)
