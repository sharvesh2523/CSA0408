import os

path = input("Enter directory path (default .): ") or "."
print("\nFiles in directory:")
for file in os.listdir(path):
    print(file)
