#!/usr/bin/env python3

matrix = [
    [30, 34, 85, 49, 12, 22, 24, 39, 29, 79],
    [4, 18, 65, 69, 89, 1, 96, 44, 41, 91],
    [57, 40, 27, 77, 62, 35, 46, 5, 43, 54],
    [66, 36, 13, 97, 93, 56, 73, 9, 90, 11],
    [75, 58, 100, 59, 32, 16, 19, 47, 94, 74],
    [71, 25, 88, 87, 99, 92, 21, 72, 28, 45],
    [84, 33, 70, 2, 52, 50, 53, 17, 48, 95],
    [51, 86, 61, 80, 14, 23, 8, 82, 26, 98],
    [67, 55, 38, 68, 64, 76, 63, 42, 3, 78],
    [7, 15, 10, 6, 20, 81, 83, 31, 60, 37]
]

# find the 7-based numbers in the matrix, and print the 1st, 2nd, and 3rd found numbers
# use nested for loops to iterate through the matrix
def find_sevens_with_break(matrix):
    sevens = []
    for row in matrix:
        for num in row:
            if num % 7 == 0:
                sevens.append(num)
                if len(sevens) == 3:
                    break
        if len(sevens) == 3:
            break
    return sevens

def find_sevens_with_return(matrix):
    sevens = []
    for row in matrix:
        for num in row:
            if num % 7 == 0:
                sevens.append(num)
                if len(sevens) == 3:
                    return sevens
    return sevens

def find_sevens_with_flag(matrix):
    sevens = []
    found_three = False
    for row in matrix:
        for num in row:
            if num % 7 == 0:
                sevens.append(num)
                if len(sevens) == 3:
                    found_three = True
                    break
        if found_three:
            break
    return sevens

def find_sevens_with_yield(matrix):
    for row in matrix:
        for num in row:
            if num % 7 == 0:
                yield num

if __name__ == '__main__':
    print("Using break:")
    sevens = find_sevens_with_break(matrix)
    for i, num in enumerate(sevens, start=1):
        print(f"The {i}st/nd/rd found 7-based number is: {num}")

    print("Using return:")
    sevens = find_sevens_with_return(matrix)
    for i, num in enumerate(sevens, start=1):
        print(f"The {i}st/nd/rd found 7-based number is: {num}")

    print("Using flag:")
    sevens = find_sevens_with_flag(matrix)
    for i, num in enumerate(sevens, start=1):
        print(f"The {i}st/nd/rd found 7-based number is: {num}")

    print("Using yield:")
    sevens_generator = find_sevens_with_yield(matrix)
    for i in range(3):
        num = next(sevens_generator)
        print(f"The {i+1}st/nd/rd found 7-based number is: {num}")
