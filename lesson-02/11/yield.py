#!/usr/bin/env python3


from typing import Iterator

def iter_squares(n: int) -> Iterator[int]:
    for i in range(n):
        print(f"Generating square for {i}")
        yield i * i
        print(f"Yielded square for {i}")


def list_squares(n) -> list[int]:
    return [i * i for i in range(n)]
    print("This line will never be executed")


if __name__ == "__main__":
    print("Using list_squares:")
    for square in list_squares(10):
        print(square)

    print("\nUsing iter_squares:")
    for square in iter_squares(10):
        print(square)