blocks = list(map(int, input("Enter block sizes (space separated): ").split()))
processes = list(map(int, input("Enter process sizes (space separated): ").split()))

print("\nFirst Fit Allocation:")
for p in processes:
    allocated = False
    for i in range(len(blocks)):
        if blocks[i] >= p:
            print(f"Process {p} -> Block {i+1}")
            blocks[i] -= p
            allocated = True
            break
    if not allocated:
        print(f"Process {p} -> Not Allocated")
