from multiprocessing import Process, Queue

def sender(q):
    msg = input("Enter message to send: ")
    q.put(msg)

def receiver(q):
    print("Receiver got:", q.get())

if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=sender, args=(q,))
    p1.start(); p1.join()
    p2 = Process(target=receiver, args=(q,))
    p2.start(); p2.join()
