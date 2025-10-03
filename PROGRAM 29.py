import threading, time
from collections import deque

buffer = deque()
MAX_SIZE = int(input("Enter buffer size: "))
lock = threading.Lock()

def producer():
    for i in range(1, 6):
        with lock:
            if len(buffer) < MAX_SIZE:
                buffer.append(i)
                print(f"Produced {i}, Buffer: {list(buffer)}")
        time.sleep(1)

def consumer():
    for _ in range(5):
        with lock:
            if buffer:
                item = buffer.popleft()
                print(f"Consumed {item}, Buffer: {list(buffer)}")
        time.sleep(2)

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start(); t2.start()
t1.join(); t2.join()
