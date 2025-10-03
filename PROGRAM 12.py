import threading, time

n = int(input("Enter number of philosophers: "))
forks = [threading.Lock() for _ in range(n)]

def philosopher(i):
    left, right = forks[i], forks[(i+1)%n]
    with left:
        with right:
            print(f"Philosopher {i+1} is eating")
            time.sleep(1)

threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(n)]
for t in threads: t.start()
for t in threads: t.join()
