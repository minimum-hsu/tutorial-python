#!/usr/bin/env python3

from threading import Thread
import time

def worker(number):
    """Thread worker function"""
    print(f'Worker {number} is running')
    time.sleep(2)
    print(f'Worker {number} has finished')

if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()