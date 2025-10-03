def fifo(pages, frames):
    memory = []
    faults = 0
    print("\nPage\tMemory")
    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            faults += 1
        print(page, "\t", memory)
    print("\nTotal Page Faults:", faults)

pages = list(map(int, input("Enter reference string (space separated): ").split()))
frames = int(input("Enter number of frames: "))
fifo(pages, frames)
