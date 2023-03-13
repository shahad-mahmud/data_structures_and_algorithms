""" 
Implementation of queue using array or list. Supported operations are: enqueue, dequeue, peek,
is_empty, and size.
"""


class Queue(object):
    def __init__(self, value: object) -> None:
        self._list = [value] if value else []

        self._size = 1 if value else 0

    def enqueue(self, value: object) -> None:
        self._list.append(value)

        self._size += 1

    def dequeue(self) -> None:
        assert not self.is_empty(), "Nothing to dequeue from the queue."

        self._list.pop(0)

        self._size -= 1

    def peek(self) -> object:
        assert not self.is_empty(), "Nothing to peek from the queue."

        return self._list[0]

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self):
        return self._size

    def __str__(self):
        res = f"{self.__class__.__name__}([{str(self._list)}])"
        return res


if __name__ == "__main__":
    q = Queue(3)
    print(q)

    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(12)
    q.enqueue(21)
    print(q)

    q.dequeue()
    print(q.peek())
    q.dequeue()
    print(q.peek())
    q.dequeue()
    print(q.peek())

    print(q)
