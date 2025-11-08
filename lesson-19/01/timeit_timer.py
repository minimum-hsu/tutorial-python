#!/usr/bin/env python3

# Using timeit module to measure execution time

import timeit

def slow_function():
    import time
    time.sleep(2)

if __name__ == "__main__":
    timer = timeit.Timer(stmt="slow_function()", setup="from __main__ import slow_function")
    execution_time = timer.timeit(number=1)
    print(f"slow_function took {execution_time:.4f} seconds to execute.")
