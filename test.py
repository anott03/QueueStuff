from normal_queue import Queue
from linked_list_queue import LLQueue
import timeit


def test_normalQ():
    q = Queue()
    for i in range(1, 1000):
        q.enqueue({i: i})
    while not q.isEmpty():
        q.dequeue()


def test_llQ():
    q = LLQueue()
    for i in range(1, 1000):
        q.enqueue({i: i})
    while not q.isEmpty():
        q.dequeue()


if __name__ == "__main__":
    T1 = timeit.Timer("test_normalQ()", "from test import test_normalQ")
    T2 = timeit.Timer("test_llQ()", "from test import test_llQ")

    print("normal queue: ", T1.timeit(1000))
    print("linked list queue: ", T2.timeit(1000))
