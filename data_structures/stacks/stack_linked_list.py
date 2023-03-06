class Node(object):
    def __init__(self, value=None, next=None, prev=None) -> None:
        self.value = value
        self.next = next
        self.prev = prev


class Stack(object):
    def __init__(self, value: object = None) -> None:
        if value:
            self._tail = Node(value)
        else:
            self._tail = None

        self._head = self._tail
        self._size = 1 if self._tail else 0

    def push(self, value: object) -> None:
        if not self._head:
            self._tail = Node(value)
            self._head = self._tail
        else:
            self._tail.next = Node(value)
            self._tail.next.prev = self._tail
            self._tail = self._tail.next

        self._size += 1

    def pop(self) -> None:
        assert not self.is_empty(), "Stack is empty. Nothing to pop."

        if self._size == 1:
            self._head = self._tail = None
        else:
            self._tail = self._tail.prev

            del self._tail.next
            self._tail.next = None

        self._size -= 1

    def peek(self) -> object:
        assert not self.is_empty(), "Stack is empty. Nothing to peek."

        return self._tail.value

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def __str__(self) -> str:
        res = self.__class__.__name__ + '['

        current = self._head
        while current:
            res += str(
                current.value) if current == self._head else f", {current.value}"
            current = current.next

        res += ']'

        return res


if __name__ == "__main__":
    s = Stack(2)

    s.push(7)
    s.push(6)

    print(s)
    print(s.peek())

    s.pop()
    print(s)
    print(s.peek())

    s.pop()
    print(s.peek())
    s.pop()  # raise error
