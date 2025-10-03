import threading, time

rw_mutex = threading.Semaphore(1)
mutex = threading.Semaphore(1)
read_count = 0

def reader(id):
    global read_count
    while True:
        mutex.acquire()
        read_count += 1
        if read_count == 1:
            rw_mutex.acquire()
        mutex.release()

        print(f"Reader {id} is reading...")
        time.sleep(1)

        mutex.acquire()
        read_count -= 1
        if read_count == 0:
            rw_mutex.release()
        mutex.release()
        time.sleep(1)

def writer(id):
    while True:
        rw_mutex.acquire()
        print(f"Writer {id} is writing...")
        time.sleep(2)
        rw_mutex.release()
        time.sleep(1)

n_r = int(input("Enter number of readers: "))
n_w = int(input("Enter number of writers: "))

threads = []
for i in range(n_r):
    t = threading.Thread(target=reader, args=(i+1,))
    threads.append(t)
    t.start()

for i in range(n_w):
    t = threading.Thread(target=writer, args=(i+1,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
