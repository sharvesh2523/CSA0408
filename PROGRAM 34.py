filename = input("Enter filename: ")
records = []

while True:
    ch = input("\n1.Add Record  2.Display File  3.Access Record  4.Exit: ")
    if ch == "1":
        rec = input("Enter record data: ")
        records.append(rec)
        print("Record added.")
    elif ch == "2":
        print("File Records:", records)
    elif ch == "3":
        idx = int(input("Enter record index to access: "))
        if 0 <= idx < len(records):
            print("Record:", records[idx])
        else:
            print("Invalid index.")
    else:
        break
