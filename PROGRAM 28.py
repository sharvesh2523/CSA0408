filename = input("Enter filename: ")
pattern = input("Enter search pattern: ")

with open(filename, "r") as f:
    for line_no, line in enumerate(f, 1):
        if pattern in line:
            print(f"Line {line_no}: {line.strip()}")
