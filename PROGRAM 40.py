import os, stat

fname = input("Enter filename: ")
with open(fname, "w") as f:
    f.write("Test file for permissions.")

print("\nCurrent Permissions (Octal):", oct(os.stat(fname).st_mode)[-3:])

print("\n1.Read Only  2.Write Only  3.Read & Write  4.Execute Only")
choice = input("Enter permission choice: ")

if choice == "1":
    os.chmod(fname, stat.S_IRUSR)
elif choice == "2":
    os.chmod(fname, stat.S_IWUSR)
elif choice == "3":
    os.chmod(fname, stat.S_IRUSR | stat.S_IWUSR)
elif choice == "4":
    os.chmod(fname, stat.S_IXUSR)

print("Updated Permissions (Octal):", oct(os.stat(fname).st_mode)[-3:])
