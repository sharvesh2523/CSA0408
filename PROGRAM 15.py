directory = []
while True:
    choice = input("\n1.Create File  2.List Files  3.Exit: ")
    if choice == "1":
        name = input("Enter file name: ")
        directory.append(name)
        print("File created.")
    elif choice == "2":
        print("Files:", directory)
    else:
        break
