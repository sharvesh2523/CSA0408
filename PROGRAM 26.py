import os

def create_file(fname):
    with open(fname, "w") as f:
        print(f"File {fname} created.")

def write_file(fname):
    text = input("Enter text to write: ")
    with open(fname, "a") as f:
        f.write(text + "\n")
    print("Data written successfully.")

def read_file(fname):
    if os.path.exists(fname):
        with open(fname, "r") as f:
            print("File content:\n", f.read())
    else:
        print("File not found.")

def delete_file(fname):
    if os.path.exists(fname):
        os.remove(fname)
        print(f"File {fname} deleted.")
    else:
        print("File not found.")

fname = input("Enter filename: ")
while True:
    print("\n1.Create  2.Write  3.Read  4.Delete  5.Exit")
    ch = input("Enter choice: ")
    if ch == "1": create_file(fname)
    elif ch == "2": write_file(fname)
    elif ch == "3": read_file(fname)
    elif ch == "4": delete_file(fname)
    else: break
