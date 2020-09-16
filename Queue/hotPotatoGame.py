from queue import Queue

def hotPotatoGame(nameList, num):
    simQueue = Queue()

    for name in nameList:
        simQueue.enqueue(name)

    while simQueue.size() > 1:
        for i in range(num):
            simQueue.enqueue(simQueue.dequeue())

        simQueue.dequeue()
    return simQueue.dequeue()  

print(hotPotatoGame(["Bill","David","Susan","Jane","Kent","Brad"], 7))              