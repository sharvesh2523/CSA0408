def scan(requests, head, direction, disk_size):
    requests.sort()
    total, order = 0, []
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    if direction == "left":
        order = left[::-1] + [0] + right
    else:
        order = right + [disk_size-1] + left[::-1]

    print("\nOrder of servicing:", order)
    for r in order:
        total += abs(r - head)
        head = r
    print("Total Head Movement:", total)

head = int(input("Enter initial head position: "))
disk_size = int(input("Enter disk size: "))
requests = list(map(int, input("Enter disk requests (space separated): ").split()))
direction = input("Enter direction (left/right): ").lower()
scan(requests, head, direction, disk_size)
