def optimal(pages, frames):
    memory = []
    faults = 0
    print("\nPage\tMemory")
    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                # find page to replace
                future = memory[:]
                for m in memory:
                    if m in pages[i+1:]:
                        future.remove(m)
                        future.append(m)
                replace = future[0]
                memory[memory.index(replace)] = page
            faults += 1
        print(page, "\t", memory)
    print("\nTotal Page Faults:", faults)

pages = list(map(int, input("Enter reference string (space separated): ").split()))
frames = int(input("Enter number of frames: "))
optimal(pages, frames)
