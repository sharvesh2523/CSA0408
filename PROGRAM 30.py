import threading, time

def worker(n):
    print(f"Thread {n} started")
    time.sleep(1)
    print(f"Thread {n} exiting")

threads = []
n = int(input("Enter number of threads: "))
for i in range(n):
    t = threading.Thread(target=worker, args=(i+1,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# equal example
if threads[0] == threads[0]:
    print("Thread 1 is equal to itself.")

print("All threads finished execution.")
