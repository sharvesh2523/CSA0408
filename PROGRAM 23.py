def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break

    print("\nProcess No.\tProcess Size\tBlock No.")
    for i in range(len(processes)):
        if allocation[i] != -1:
            print(i+1, "\t\t", processes[i], "\t\t", allocation[i]+1)
        else:
            print(i+1, "\t\t", processes[i], "\t\tNot Allocated")

blocks = list(map(int, input("Enter block sizes (space separated): ").split()))
processes = list(map(int, input("Enter process sizes (space separated): ").split()))
first_fit(blocks, processes)
