def lru(pages, frames):
    memory = []
    faults = 0
    recent = {}
    print("\nPage\tMemory")
    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                # replace least recently used
                lru_page = min(recent, key=recent.get)
                memory[memory.index(lru_page)] = page
            faults += 1
        recent[page] = i
        print(page, "\t", memory)
    print("\nTotal Page Faults:", faults)

pages = list(map(int, input("Enter reference string (space separated): ").split()))
frames = int(input("Enter number of frames: "))
lru(pages, frames)
