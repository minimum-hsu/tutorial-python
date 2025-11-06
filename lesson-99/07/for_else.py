#!/usr/bin/env python3

if __name__ == '__main__':
    # Find out the prime numbers in a given range
    for num in range(2, 100):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(f"{num} is prime")
            # The else block executes only if the loop wasn't broken out of
