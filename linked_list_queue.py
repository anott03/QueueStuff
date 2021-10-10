class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def getNext(self):
        return self.next

    def getData(self):
        return self.data

    def setNext(self, n):
        self.next = n

    def setData(self, d):
        self.data = d


class LLQueue:
    def __init__(self):
        self.head = Node(None)
        self._size = 0

    def enqueue(self, item):
        nn = Node(item)
        if self.head.getNext() is not None:
            nn.setNext(self.head.getNext())
        self.head.setNext(nn)
        self._size += 1

    def dequeue(self):
        if self.head.getNext() is not None:
            item = self.head.getNext()
            self.head.setNext(item.getNext())
            self._size -= 1
            return item.getData()

        return None

    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0
