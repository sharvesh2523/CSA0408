files = {}

while True:
    ch = input("\n1.Create File  2.Add Block  3.Display File  4.Exit: ")
    if ch == "1":
        fname = input("Enter file name: ")
        files[fname] = []
        print("File created.")
    elif ch == "2":
        fname = input("Enter file name: ")
        if fname in files:
            block = input("Enter block data: ")
            files[fname].append(block)
            print("Block linked.")
        else:
            print("File not found.")
    elif ch == "3":
        for fname, blocks in files.items():
            print(fname, "->", " -> ".join(blocks) if blocks else "Empty")
    else:
        break
