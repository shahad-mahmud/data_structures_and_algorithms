class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        s = self.__class__.__name__ + "{"
        s += f"value: {self.value}, next: {self.next}"
        s += "}"

        return s


class SinglyLinkedList(object):
    def __init__(self, value: object = None, node: Node = None) -> None:
        if value and node:
            raise ValueError(
                "Either value or node can be set at the initialization but found both set.")

        self._size = 0

        if value:
            self._cursor = Node(value)
            self._size += 1
        elif node:
            self._cursor = node
            self._size += 1
        else:
            self._cursor = None

        self._head = self._cursor

    def add(self, value: object) -> None:
        """
        Add an object at the end of the list.

        args:
            value (object): The object to add in the list
        """
        if self._head is None:
            self._cursor = Node(value)
            self._head = self._cursor
        else:
            temp = Node(value)
            self._cursor.next = temp
            self._cursor = temp

        self._size += 1

    def insert(self, position: int, value: object) -> None:
        """
        Insert an object at the given position of the list. If the position is equal to the
        length of the list, it is similar to adding an object at the end.

        args:
            position (int): The position at which the object will be inserted.
            value (object): The object to add in the list
        """
        assert position <= self._size, ("Position must be less than or equal to the length of "
                                        "the list.")

        if position == self._size:
            self.add(value)
        elif position == 0:
            temp = Node(value)
            temp.next = self._head

            self._head = temp
            self._size += 1
        else:
            i, current, previous = 0, self._head.next, self._head

            while i < position-1 and current:
                current = current.next
                previous = previous.next
                i += 1

            temp = Node(value)
            temp.next = current
            previous.next = temp

            self._size += 1

    def remove(self, position: int) -> None:
        """
        Remove an object from the given position in the list.

        args:
            position (int): The postion from which the object will be removed
        """
        assert position < self._size, "Position must be less than the length of the list."

        if position == 0:
            self._head = self._head.next
        else:
            i, previous, current = 1, self._head, self._head.next

            while i < position and current:
                previous = previous.next
                current = current.next
                i += 1

            previous.next = current.next if current else None
            del current  # prevent memory leak

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def __str__(self) -> str:
        s = self.__class__.__name__ + "("
        s += str(self._head)
        s += ")"

        return s


if __name__ == '__main__':
    l = SinglyLinkedList()

    l.add(1)
    l.add(13)
    l.add(16)
    l.add(19)
    l.add(26)

    print(l)

    l.insert(4, 20)
    print(l)

    l.insert(0, 0)
    print(l)

    l.insert(7, 30)
    print(l)

    l.insert(7, 28)
    print(l)
    print(l.size())

    l.remove(3)
    print(l)

    l.remove(0)
    print(l)

    l.remove(6)
    print(l)
