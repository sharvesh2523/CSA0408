import os

filename = input("Enter filename: ")

while True:
    print("\n1.Create File  2.Write File  3.Read File  4.Delete File  5.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        open(filename, "w").close()
        print("File created.")
    elif ch == "2":
        text = input("Enter text to write: ")
        with open(filename, "a") as f:
            f.write(text + "\n")
        print("Written successfully.")
    elif ch == "3":
        if os.path.exists(filename):
            with open(filename, "r") as f:
                print("File content:\n", f.read())
        else:
            print("File not found.")
    elif ch == "4":
        if os.path.exists(filename):
            os.remove(filename)
            print("File deleted.")
        else:
            print("File not found.")
    else:
        break
