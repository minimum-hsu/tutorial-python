#!/usr/bin/env python3

from multiprocessing import Process
import os
import time

def worker(number):
    """Process worker function"""
    print(f'Process {number} is running')
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    time.sleep(2)
    print(f'Process {number} has finished')

if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
