import threading, time

lock = threading.Lock()
counter = 0

def task(name):
    global counter
    for _ in range(3):
        lock.acquire()
        print(f"{name} entered critical section.")
        counter += 1
        time.sleep(1)
        print(f"{name} leaving critical section. Counter = {counter}")
        lock.release()
        time.sleep(1)

n = int(input("Enter number of processes (threads): "))
threads = [threading.Thread(target=task, args=(f"Process-{i+1}",)) for i in range(n)]
for t in threads: t.start()
for t in threads: t.join()
