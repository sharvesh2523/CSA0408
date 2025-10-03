def fcfs(requests, head):
    total = 0
    print("\nOrder of requests:")
    for r in requests:
        print(r, end=" ")
        total += abs(r - head)
        head = r
    print("\nTotal Head Movement:", total)

head = int(input("Enter initial head position: "))
requests = list(map(int, input("Enter disk requests (space separated): ").split()))
fcfs(requests, head)
