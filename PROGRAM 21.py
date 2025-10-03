def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        worst_index = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if worst_index == -1 or blocks[j] > blocks[worst_index]:
                    worst_index = j
        if worst_index != -1:
            allocation[i] = worst_index
            blocks[worst_index] -= processes[i]

    print("\nProcess No.\tProcess Size\tBlock No.")
    for i in range(len(processes)):
        if allocation[i] != -1:
            print(i+1, "\t\t", processes[i], "\t\t", allocation[i]+1)
        else:
            print(i+1, "\t\t", processes[i], "\t\tNot Allocated")

blocks = list(map(int, input("Enter block sizes (space separated): ").split()))
processes = list(map(int, input("Enter process sizes (space separated): ").split()))
worst_fit(blocks, processes)
