def bankers_algorithm(n, m, alloc, max_need, avail):
    need = [[max_need[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]
    finish = [False] * n
    safe_seq = []
    
    print("\nNeed Matrix:")
    for row in need:
        print(row)

    while len(safe_seq) < n:
        found = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= avail[j] for j in range(m)):
                avail = [avail[j] + alloc[i][j] for j in range(m)]
                safe_seq.append(i)
                finish[i] = True
                found = True
        if not found:
            print("System is in Deadlock state!")
            return
    print("System is in Safe State.")
    print("Safe Sequence:", ["P"+str(i) for i in safe_seq])

n = int(input("Enter number of processes: "))
m = int(input("Enter number of resources: "))
print("Enter Allocation Matrix:")
alloc = [list(map(int, input().split())) for _ in range(n)]
print("Enter Max Matrix:")
max_need = [list(map(int, input().split())) for _ in range(n)]
avail = list(map(int, input("Enter Available Resources: ").split()))

bankers_algorithm(n, m, alloc, max_need, avail)
