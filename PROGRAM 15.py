dirs = {}
while True:
    choice = input("\n1.Create Dir  2.Create File  3.List  4.Exit: ")
    if choice == "1":
        d = input("Enter directory name: ")
        dirs[d] = []
        print("Directory created.")
    elif choice == "2":
        d = input("Enter directory name: ")
        if d in dirs:
            f = input("Enter file name: ")
            dirs[d].append(f)
            print("File created.")
        else:
            print("Directory not found!")
    elif choice == "3":
        for d, files in dirs.items():
            print(d, ":", files)
    else:
        break
