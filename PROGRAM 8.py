n = int(input("Enter number of processes: "))
processes = [f"P{i+1}" for i in range(n)]
burst_time = []
for i in range(n):
    burst_time.append(int(input(f"Enter burst time for {processes[i]}: ")))

quantum = int(input("Enter time quantum: "))
remain = burst_time[:]
time = 0

print("Execution order:")
while any(r > 0 for r in remain):
    for i in range(n):
        if remain[i] > 0:
            run = min(quantum, remain[i])
            remain[i] -= run
            time += run
            print(processes[i], "->", end=" ")
print("\nTotal time:", time)
