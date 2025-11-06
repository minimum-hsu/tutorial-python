#!/usr/bin/env python3

# try-except-else-finally example
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print('Error: Division by zero!')
    else:
        print('Division successful, result is:', result)
    finally:
        print('Execution of divide() is complete.')

def open_file(filename: str):
    # handle file operations with try-except-else-finally blocks
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        print('Error: File not found!')
    else:
        content = f.read()
        print('File content:', content)
    finally:
        print('Closing file...')
        try:
            f.close()
        except NameError as e:
            # File was never opened
            pass

if __name__ == '__main__':
    divide(10, 2)
    divide(10, 0)
    open_file('data.txt')
