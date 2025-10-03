import os

filename = "employees.txt"

def add_employee():
    with open(filename, "a") as f:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        salary = input("Enter Salary: ")
        f.write(f"{emp_id},{name},{salary}\n")
    print("Employee added successfully.")

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    with open(filename, "r") as f:
        for line in f:
            eid, name, sal = line.strip().split(",")
            if eid == emp_id:
                print(f"ID: {eid}, Name: {name}, Salary: {sal}")
                found = True
    if not found:
        print("Employee not found.")

while True:
    ch = input("\n1.Add Employee  2.Search Employee  3.Exit: ")
    if ch == "1":
        add_employee()
    elif ch == "2":
        search_employee()
    else:
        break
