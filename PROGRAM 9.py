from multiprocessing import Process, Value

def writer(val):
    val.value = int(input("Enter a value to write: "))
    print("Writer set value:", val.value)

def reader(val):
    print("Reader got value:", val.value)

if __name__ == "__main__":
    num = Value('i', 0)
    p1 = Process(target=writer, args=(num,))
    p1.start(); p1.join()
    p2 = Process(target=reader, args=(num,))
    p2.start(); p2.join()
