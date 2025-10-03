import heapq

processes = [("P1", 5, 2), ("P2", 3, 1), ("P3", 8, 3)]  # (name, burst, priority)
pq = []
for p in processes:
    heapq.heappush(pq, (p[2], p[1], p[0]))  # priority first

time = 0
print("Order of execution:")
while pq:
    pr, bt, name = heapq.heappop(pq)
    print(name, "->", end=" ")
    time += bt
print("\nTotal time:", time)
