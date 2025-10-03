import threading

def worker(n):
    print(f"Thread {n} is running")

n = int(input("Enter number of threads: "))
threads = []
for i in range(n):
    t = threading.Thread(target=worker, args=(i+1,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
