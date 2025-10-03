import os

filename = input("Enter filename: ")
with open(filename, "w") as f:
    f.write("Hello Operating Systems!\nThis is a sample file.\n")

# SEEK example
with open(filename, "r") as f:
    f.seek(6)  # move cursor
    print("Seek Example:", f.read(9))

# STAT example
info = os.stat(filename)
print("\nFile Stat:")
print("Size:", info.st_size, "bytes")
print("Permissions:", oct(info.st_mode)[-3:])

# OPENDIR and READDIR example
path = "."
print("\nFiles in current directory:")
for file in os.listdir(path):
    print(file)
