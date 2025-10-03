def cscan(requests, head, disk_size):
    requests.sort()
    total, order = 0, []
    right = [r for r in requests if r >= head]
    left = [r for r in requests if r < head]

    order = right + [disk_size-1, 0] + left
    print("\nOrder of servicing:", order)

    for r in order:
        total += abs(r - head)
        head = r
    print("Total Head Movement:", total)

head = int(input("Enter initial head position: "))
disk_size = int(input("Enter disk size: "))
requests = list(map(int, input("Enter disk requests (space separated): ").split()))
cscan(requests, head, disk_size)
