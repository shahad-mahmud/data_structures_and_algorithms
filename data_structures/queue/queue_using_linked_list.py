""" 
Implementation of queue using Linked List. Supported operations are: enqueue, dequeue, peek, 
is_empty, and size.
"""


class Node(object):
    def __init__(self, value: object, next=None) -> None:
        self.value = value
        self.next = next


class Queue(object):
    def __init__(self, value: object) -> None:
        if value:
            self._tail = Node(value)
        else:
            self._tail = None

        self._head = self._tail
        self._size = 1 if value else 0

    def enqueue(self, value: object) -> None:
        if not self._head:
            self._tail = Node(value)
            self._head = self._tail
        else:
            self._tail.next = Node(value)
            self._tail = self._tail.next

        self._size += 1

    def dequeue(self) -> None:
        assert not self.is_empty(), "Nothing to dequeue from the queue."

        if not self._head.next:
            del self._head
            self._head = None

        temp = self._head
        self._head = self._head.next
        del temp

        self._size -= 1

    def peek(self) -> object:
        assert not self.is_empty(), "Nothing to peek from the queue."

        return self._head.value

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self):
        return self._size

    def __str__(self):
        res = f"{self.__class__.__name__}(["

        current = self._head
        while current:
            res += str(
                current.value) if current == self._head else f", {current.value}"
            current = current.next

        res += '])'
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
