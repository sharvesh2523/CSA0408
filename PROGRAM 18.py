import threading, time
from collections import deque

buffer = deque()
MAX_SIZE = int(input("Enter buffer size: "))
mutex = threading.Semaphore(1)
empty = threading.Semaphore(MAX_SIZE)
full = threading.Semaphore(0)

def producer():
    for i in range(1, 6):
        empty.acquire()
        mutex.acquire()
        buffer.append(i)
        print(f"Produced: {i}")
        mutex.release()
        full.release()
        time.sleep(1)

def consumer():
    for _ in range(5):
        full.acquire()
        mutex.acquire()
        item = buffer.popleft()
        print(f"Consumed: {item}")
        mutex.release()
        empty.release()
        time.sleep(2)

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start(); t2.start()
t1.join(); t2.join()
