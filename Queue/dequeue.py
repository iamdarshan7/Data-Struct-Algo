class Dequeue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

d = Dequeue()
d.addFront(5)                                
d.addFront('Yes')                                
d.addFront(True)

while not d.isEmpty():
    print(d.removeFront())