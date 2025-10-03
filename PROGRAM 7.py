n = int(input("Enter number of processes: "))
processes = []
for i in range(n):
    bt = int(input(f"Enter burst time for P{i+1}: "))
    processes.append((f"P{i+1}", bt))

processes.sort(key=lambda x: x[1])

time = 0
print("Process\tBurst\tWaiting\tTurnaround")
for name, bt in processes:
    print(name, "\t", bt, "\t", time, "\t", time + bt)
    time += bt
