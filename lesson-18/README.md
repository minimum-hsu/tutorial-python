# Lesson 18 - Concurrent Programming  <!-- omit in toc -->

This lesson covers concurrent programming in Python using both threading and multiprocessing approaches, demonstrating how to execute code in parallel to improve performance and handle concurrent tasks.

<!-- TOC -->
- [Learning Objectives](#learning-objectives)
- [Course Content](#course-content)
  - [01. Threading - Concurrent Execution with Threads](#01-threading---concurrent-execution-with-threads)
  - [02. Multiprocessing - Parallel Execution with Processes](#02-multiprocessing---parallel-execution-with-processes)
- [Threading vs Multiprocessing Comparison](#threading-vs-multiprocessing-comparison)
  - [Feature Comparison](#feature-comparison)
  - [When to Use Each](#when-to-use-each)
    - [Use Threading when:](#use-threading-when)
    - [Use Multiprocessing when:](#use-multiprocessing-when)
- [Advanced Concurrent Programming Patterns](#advanced-concurrent-programming-patterns)
  - [Thread Synchronization](#thread-synchronization)
  - [Process Communication](#process-communication)
  - [Thread Pool and Process Pool](#thread-pool-and-process-pool)
  - [Asynchronous Programming](#asynchronous-programming)
- [Practical Examples](#practical-examples)
  - [Web Scraper with Threading](#web-scraper-with-threading)
  - [CPU-Intensive Task with Multiprocessing](#cpu-intensive-task-with-multiprocessing)
- [How to Run Examples](#how-to-run-examples)
  - [Threading Example](#threading-example)
  - [Multiprocessing Example](#multiprocessing-example)
- [Best Practices](#best-practices)
  - [1. **Choose the Right Concurrency Model**](#1-choose-the-right-concurrency-model)
  - [2. **Proper Resource Management**](#2-proper-resource-management)
  - [3. **Handle Exceptions Properly**](#3-handle-exceptions-properly)
  - [4. **Use Thread/Process Pools**](#4-use-threadprocess-pools)
  - [5. **Avoid Common Pitfalls**](#5-avoid-common-pitfalls)
- [Performance Considerations](#performance-considerations)
  - [Understanding the GIL](#understanding-the-gil)
- [Common Concurrency Patterns](#common-concurrency-patterns)
  - [Producer-Consumer](#producer-consumer)
  - [Worker Pool](#worker-pool)
- [Practice Suggestions](#practice-suggestions)
- [Common Pitfalls](#common-pitfalls)
- [Related Resources](#related-resources)
<!-- /TOC -->

## Learning Objectives

- Understand concurrent programming concepts
- Master Python's threading module
- Learn multiprocessing for CPU-intensive tasks
- Compare threading vs multiprocessing approaches
- Handle synchronization and communication between threads/processes
- Understand the Global Interpreter Lock (GIL) and its implications
- Design scalable concurrent applications
- Handle common concurrency pitfalls and best practices

## Course Content

### 01. Threading - Concurrent Execution with Threads
**File:** `01/thread.py`

Learn concurrent programming using Python's threading module:

```python
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
```

**Key Concepts:**
- `Thread` class for creating concurrent threads
- `target` parameter for specifying worker function
- `args` parameter for passing arguments to worker
- `start()` method to begin thread execution
- `join()` method to wait for thread completion
- Shared memory space between threads
- I/O-bound task optimization

### 02. Multiprocessing - Parallel Execution with Processes
**File:** `02/process.py`

Learn parallel programming using Python's multiprocessing module:

```python
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
```

**Key Concepts:**
- `Process` class for creating separate processes
- `os.getpid()` and `os.getppid()` for process identification
- Separate memory space for each process
- CPU-bound task optimization
- Process isolation and independence
- `__name__ == '__main__'` guard for process spawning

## Threading vs Multiprocessing Comparison

### Feature Comparison

| Feature | Threading | Multiprocessing |
|---------|-----------|-----------------|
| **Memory Sharing** | Shared | Isolated |
| **GIL Impact** | Limited by GIL | No GIL limitation |
| **Overhead** | Low | High |
| **Communication** | Easy (shared memory) | Complex (IPC required) |
| **Fault Tolerance** | One thread crash affects all | Process isolation |
| **Best For** | I/O-bound tasks | CPU-bound tasks |
| **Debugging** | More complex | Easier (isolated) |
| **Resource Usage** | Lower | Higher |

### When to Use Each

#### Use Threading when:
- I/O-bound operations (file reading, network requests)
- Tasks that wait for external resources
- Need shared state between workers
- Low resource overhead required
- Coordinating multiple concurrent operations

#### Use Multiprocessing when:
- CPU-intensive computations
- Mathematical calculations
- Data processing and analysis
- Need true parallelism
- Fault isolation is important

## Advanced Concurrent Programming Patterns

### Thread Synchronization
```python
import threading
import time
from queue import Queue

# Thread-safe counter with Lock
class SafeCounter:
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self._value += 1

    @property
    def value(self):
        return self._value

# Producer-Consumer pattern with Queue
def producer(queue, items):
    for item in items:
        print(f"Producing {item}")
        queue.put(item)
        time.sleep(0.1)
    queue.put(None)  # Signal completion

def consumer(queue, worker_id):
    while True:
        item = queue.get()
        if item is None:
            queue.put(None)  # Re-queue sentinel for other consumers
            break
        print(f"Consumer {worker_id} processing {item}")
        time.sleep(0.5)
        queue.task_done()

# Usage example
def threading_example():
    # Counter example
    counter = SafeCounter()
    threads = []

    def increment_worker():
        for _ in range(1000):
            counter.increment()

    for _ in range(5):
        t = threading.Thread(target=increment_worker)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Final counter value: {counter.value}")

    # Producer-Consumer example
    queue = Queue()
    items = list(range(10))

    # Start producer
    producer_thread = threading.Thread(target=producer, args=(queue, items))
    producer_thread.start()

    # Start consumers
    consumer_threads = []
    for i in range(3):
        t = threading.Thread(target=consumer, args=(queue, i))
        consumer_threads.append(t)
        t.start()

    # Wait for completion
    producer_thread.join()
    for t in consumer_threads:
        t.join()
```

### Process Communication
```python
import multiprocessing
import time
from multiprocessing import Queue, Pipe, Value, Array

def worker_with_queue(queue, worker_id):
    """Worker that communicates via Queue"""
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Process {worker_id} processing {item}")
        result = item ** 2
        queue.put(f"Result: {result}")

def worker_with_pipe(conn, data):
    """Worker that communicates via Pipe"""
    for item in data:
        result = item ** 2
        conn.send(result)
    conn.close()

def worker_with_shared_memory(shared_value, shared_array, start, end):
    """Worker that uses shared memory"""
    for i in range(start, end):
        shared_array[i] = shared_array[i] ** 2

    with shared_value.get_lock():
        shared_value.value += 1

def multiprocessing_examples():
    # Queue example
    queue = Queue()
    processes = []

    # Add work items
    for i in range(10):
        queue.put(i)

    # Start worker processes
    for i in range(3):
        p = multiprocessing.Process(target=worker_with_queue, args=(queue, i))
        processes.append(p)
        p.start()

    # Signal completion
    for _ in range(3):
        queue.put(None)

    for p in processes:
        p.join()

    # Pipe example
    parent_conn, child_conn = Pipe()
    data = [1, 2, 3, 4, 5]
    p = multiprocessing.Process(target=worker_with_pipe, args=(child_conn, data))
    p.start()

    # Receive results
    for _ in data:
        result = parent_conn.recv()
        print(f"Received: {result}")

    p.join()

    # Shared memory example
    shared_value = Value('i', 0)
    shared_array = Array('i', range(10))

    processes = []
    for i in range(0, 10, 2):
        p = multiprocessing.Process(
            target=worker_with_shared_memory,
            args=(shared_value, shared_array, i, min(i+2, 10))
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Shared value: {shared_value.value}")
    print(f"Shared array: {list(shared_array[:])}")
```

### Thread Pool and Process Pool
```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import requests

def cpu_bound_task(n):
    """CPU-intensive task"""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

def io_bound_task(url):
    """I/O-bound task"""
    try:
        response = requests.get(url, timeout=5)
        return len(response.content)
    except:
        return 0

def pool_examples():
    # ThreadPoolExecutor for I/O-bound tasks
    urls = [
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/1',
    ]

    print("ThreadPoolExecutor for I/O-bound tasks:")
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(io_bound_task, url) for url in urls]
        results = [future.result() for future in futures]

    print(f"Results: {results}")
    print(f"Time taken: {time.time() - start_time:.2f} seconds")

    # ProcessPoolExecutor for CPU-bound tasks
    numbers = [100000, 100000, 100000, 100000]

    print("\nProcessPoolExecutor for CPU-bound tasks:")
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(cpu_bound_task, n) for n in numbers]
        results = [future.result() for future in futures]

    print(f"Results: {results}")
    print(f"Time taken: {time.time() - start_time:.2f} seconds")
```

### Asynchronous Programming
```python
import asyncio
import aiohttp
import time

async def async_fetch(session, url):
    """Asynchronous HTTP request"""
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as e:
        return f"Error: {e}"

async def async_cpu_task(n):
    """CPU task with async/await (not truly parallel)"""
    total = 0
    for i in range(n):
        total += i ** 2
        if i % 10000 == 0:
            await asyncio.sleep(0)  # Yield control
    return total

async def async_examples():
    # Async I/O operations
    urls = [
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/1',
    ]

    print("Asynchronous I/O operations:")
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [async_fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    print(f"Completed {len(results)} requests")
    print(f"Time taken: {time.time() - start_time:.2f} seconds")

    # Async CPU tasks (cooperative multitasking)
    print("\nAsynchronous CPU tasks:")
    start_time = time.time()

    tasks = [async_cpu_task(50000) for _ in range(4)]
    results = await asyncio.gather(*tasks)

    print(f"Results: {results}")
    print(f"Time taken: {time.time() - start_time:.2f} seconds")

# Run async examples
# asyncio.run(async_examples())
```

## Practical Examples

### Web Scraper with Threading
```python
import threading
import requests
from queue import Queue
import time

class WebScraper:
    def __init__(self, max_workers=5):
        self.max_workers = max_workers
        self.url_queue = Queue()
        self.result_queue = Queue()
        self.workers = []

    def worker(self):
        """Worker thread function"""
        while True:
            url = self.url_queue.get()
            if url is None:
                break

            try:
                response = requests.get(url, timeout=10)
                result = {
                    'url': url,
                    'status_code': response.status_code,
                    'content_length': len(response.content),
                    'title': self.extract_title(response.text)
                }
                self.result_queue.put(result)
            except Exception as e:
                self.result_queue.put({
                    'url': url,
                    'error': str(e)
                })
            finally:
                self.url_queue.task_done()

    def extract_title(self, html):
        """Simple title extraction"""
        import re
        match = re.search(r'<title[^>]*>([^<]+)</title>', html, re.IGNORECASE)
        return match.group(1).strip() if match else "No title"

    def scrape(self, urls):
        """Scrape multiple URLs concurrently"""
        # Add URLs to queue
        for url in urls:
            self.url_queue.put(url)

        # Start worker threads
        for _ in range(min(self.max_workers, len(urls))):
            t = threading.Thread(target=self.worker)
            t.daemon = True
            self.workers.append(t)
            t.start()

        # Wait for all tasks to complete
        self.url_queue.join()

        # Stop workers
        for _ in self.workers:
            self.url_queue.put(None)

        for t in self.workers:
            t.join()

        # Collect results
        results = []
        while not self.result_queue.empty():
            results.append(self.result_queue.get())

        return results

# Usage
scraper = WebScraper(max_workers=5)
urls = [
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/2',
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/1',
]

start_time = time.time()
results = scraper.scrape(urls)
print(f"Scraped {len(results)} URLs in {time.time() - start_time:.2f} seconds")
```

### CPU-Intensive Task with Multiprocessing
```python
import multiprocessing
import time
import math

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """Find all prime numbers in a range"""
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    return primes

def parallel_prime_finder(max_number, num_processes=None):
    """Find primes using multiple processes"""
    if num_processes is None:
        num_processes = multiprocessing.cpu_count()

    # Divide work among processes
    chunk_size = max_number // num_processes
    ranges = []

    for i in range(num_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_processes - 1 else max_number
        ranges.append((start, end))

    # Use process pool to find primes
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.starmap(find_primes_in_range, ranges)

    # Combine results
    all_primes = []
    for prime_list in results:
        all_primes.extend(prime_list)

    return sorted(all_primes)

# Compare sequential vs parallel execution
def compare_performance():
    max_num = 10000

    # Sequential execution
    print("Sequential execution:")
    start_time = time.time()
    sequential_primes = find_primes_in_range(0, max_num)
    sequential_time = time.time() - start_time
    print(f"Found {len(sequential_primes)} primes in {sequential_time:.2f} seconds")

    # Parallel execution
    print("\nParallel execution:")
    start_time = time.time()
    parallel_primes = parallel_prime_finder(max_num)
    parallel_time = time.time() - start_time
    print(f"Found {len(parallel_primes)} primes in {parallel_time:.2f} seconds")

    # Verify results are the same
    print(f"\nResults match: {sequential_primes == parallel_primes}")
    print(f"Speedup: {sequential_time / parallel_time:.2f}x")

# compare_performance()
```

## How to Run Examples

### Threading Example
```bash
# Navigate to corresponding directory
cd lesson-18/01
python3 thread.py
```

### Multiprocessing Example
```bash
cd lesson-18/02
python3 process.py
```

## Best Practices

### 1. **Choose the Right Concurrency Model**
```python
# Good: Use threading for I/O-bound tasks
import threading
import requests

def fetch_url(url):
    response = requests.get(url)
    return response.status_code

urls = ['http://example.com', 'http://google.com']
threads = []
for url in urls:
    t = threading.Thread(target=fetch_url, args=(url,))
    threads.append(t)
    t.start()

# Good: Use multiprocessing for CPU-bound tasks
import multiprocessing

def cpu_intensive_task(data):
    return sum(x**2 for x in data)

data_chunks = [[1,2,3], [4,5,6], [7,8,9]]
with multiprocessing.Pool() as pool:
    results = pool.map(cpu_intensive_task, data_chunks)
```

### 2. **Proper Resource Management**
```python
# Good: Use context managers or try/finally
import threading

lock = threading.Lock()

def safe_operation():
    with lock:  # Automatically releases lock
        # Critical section
        pass

# Good: Clean shutdown of threads
import threading
import time

shutdown_event = threading.Event()

def worker():
    while not shutdown_event.is_set():
        # Do work
        time.sleep(0.1)

# Signal shutdown
shutdown_event.set()
```

### 3. **Handle Exceptions Properly**
```python
# Good: Exception handling in threads
import threading
import logging

def worker_with_exception_handling():
    try:
        # Potentially risky operation
        risky_operation()
    except Exception as e:
        logging.error(f"Worker failed: {e}")
        # Don't let exceptions kill the thread silently

# Good: Exception handling in processes
def safe_worker(data):
    try:
        return process_data(data)
    except Exception as e:
        return f"Error: {e}"
```

### 4. **Use Thread/Process Pools**
```python
# Good: Use pools for managing workers
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Thread pool for I/O
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(io_task, data) for data in dataset]
    results = [f.result() for f in futures]

# Process pool for CPU work
with ProcessPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(cpu_task, data) for data in dataset]
    results = [f.result() for f in futures]
```

### 5. **Avoid Common Pitfalls**
```python
# Avoid: Race conditions
# Bad
counter = 0
def increment():
    global counter
    counter += 1  # Not thread-safe

# Good: Use locks or atomic operations
import threading
counter = 0
lock = threading.Lock()

def safe_increment():
    global counter
    with lock:
        counter += 1

# Avoid: Deadlocks
# Bad: Different lock ordering in different threads
def thread1():
    lock1.acquire()
    lock2.acquire()  # Potential deadlock
    # work
    lock2.release()
    lock1.release()

def thread2():
    lock2.acquire()
    lock1.acquire()  # Potential deadlock
    # work
    lock1.release()
    lock2.release()

# Good: Consistent lock ordering
def safe_thread1():
    with lock1:
        with lock2:
            # work
            pass
```

## Performance Considerations

### Understanding the GIL
```python
import threading
import time

def cpu_bound_thread():
    # This won't run in parallel due to GIL
    total = 0
    for i in range(10**6):
        total += i**2
    return total

def io_bound_thread():
    # This can run concurrently (GIL released during I/O)
    time.sleep(1)
    return "Done"

# GIL limitation demonstration
start = time.time()
threads = []
for _ in range(4):
    t = threading.Thread(target=cpu_bound_thread)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Threading CPU-bound: {time.time() - start:.2f}s")

# Multiprocessing bypasses GIL
import multiprocessing

start = time.time()
with multiprocessing.Pool(4) as pool:
    results = pool.map(cpu_bound_thread, range(4))

print(f"Multiprocessing CPU-bound: {time.time() - start:.2f}s")
```

## Common Concurrency Patterns

### Producer-Consumer
```python
import threading
from queue import Queue
import time
import random

def producer(queue, producer_id):
    for i in range(5):
        item = f"Item-{producer_id}-{i}"
        queue.put(item)
        print(f"Producer {producer_id} produced {item}")
        time.sleep(random.uniform(0.1, 0.5))

def consumer(queue, consumer_id):
    while True:
        try:
            item = queue.get(timeout=2)
            print(f"Consumer {consumer_id} consumed {item}")
            time.sleep(random.uniform(0.2, 0.8))
            queue.task_done()
        except:
            break

# Usage
queue = Queue(maxsize=10)
threads = []

# Start producers
for i in range(2):
    t = threading.Thread(target=producer, args=(queue, i))
    threads.append(t)
    t.start()

# Start consumers
for i in range(3):
    t = threading.Thread(target=consumer, args=(queue, i))
    t.daemon = True
    threads.append(t)
    t.start()

# Wait for producers to finish
for t in threads[:2]:
    t.join()

# Wait for queue to be empty
queue.join()
```

### Worker Pool
```python
import threading
from queue import Queue
import time

class WorkerPool:
    def __init__(self, num_workers=5):
        self.num_workers = num_workers
        self.task_queue = Queue()
        self.workers = []
        self.shutdown = False

    def start(self):
        for i in range(self.num_workers):
            worker = threading.Thread(target=self._worker, args=(i,))
            worker.daemon = True
            self.workers.append(worker)
            worker.start()

    def _worker(self, worker_id):
        while not self.shutdown:
            try:
                task_func, args, kwargs = self.task_queue.get(timeout=1)
                print(f"Worker {worker_id} executing task")
                result = task_func(*args, **kwargs)
                print(f"Worker {worker_id} completed task: {result}")
                self.task_queue.task_done()
            except:
                continue

    def submit(self, func, *args, **kwargs):
        self.task_queue.put((func, args, kwargs))

    def shutdown_pool(self):
        self.task_queue.join()  # Wait for all tasks
        self.shutdown = True
        for worker in self.workers:
            worker.join()

# Usage example
def sample_task(x, y):
    time.sleep(1)
    return x + y

pool = WorkerPool(num_workers=3)
pool.start()

# Submit tasks
for i in range(10):
    pool.submit(sample_task, i, i*2)

pool.shutdown_pool()
```

## Practice Suggestions

1. **Download Manager**: Build a multi-threaded file downloader
2. **Web Crawler**: Create a concurrent web scraping system
3. **Image Processor**: Process images in parallel using multiprocessing
4. **Chat Server**: Build a threaded chat server handling multiple clients
5. **Data Pipeline**: Create a multi-stage data processing pipeline
6. **Load Tester**: Build a tool to test web services with concurrent requests

## Common Pitfalls

- **Race conditions**: Shared data modification without proper synchronization
- **Deadlocks**: Circular waiting for resources between threads/processes
- **Resource leaks**: Not properly closing threads/processes or releasing resources
- **GIL limitations**: Using threading for CPU-bound tasks
- **Excessive context switching**: Creating too many threads/processes
- **Improper exception handling**: Letting exceptions kill workers silently
- **Memory sharing issues**: Incorrect use of shared memory in multiprocessing

## Related Resources

- [threading Documentation](https://docs.python.org/3/library/threading.html)
- [multiprocessing Documentation](https://docs.python.org/3/library/multiprocessing.html)
- [concurrent.futures Documentation](https://docs.python.org/3/library/concurrent.futures.html)
- [asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [Global Interpreter Lock (GIL)](https://wiki.python.org/moin/GlobalInterpreterLock)
- [Python Concurrency Patterns](https://realpython.com/python-concurrency/)

[def]: #02-multiprocessing---parallel-execution-with-processes