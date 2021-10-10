class Queue:
    def __init__(self):
        self.data = []
        self._size = 0

    def __str__(self):
        return self.data.__str__()

    def enqueue(self, item):
        self.data.insert(0, item)
        self._size += 1

    def dequeue(self):
        if self._size >= 1:
            self._size -= 1
            return self.data.pop(0)

        return None

    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0
