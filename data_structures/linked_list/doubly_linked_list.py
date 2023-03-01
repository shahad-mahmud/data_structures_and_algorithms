class Node(object):
    def __init__(self, value: object = None, next=None, prev=None) -> None:
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        res = self.__class__.__name__ + "{"
        res += f"value: {self.value}, next: {self.next}, prev: {self.prev}"
        res += "}"

        return res


class DoublyLinkedList(object):
    def __init__(self, *values):
        self._head = self._cursor = None
        self._size = 0

        for value in values:
            self.add(value)

    def add(self, value: object):
        """Adds a value at the end of the list.

        Args:
            value (object): The object to add.
        """
        if not self._head:
            self._cursor = Node(value)
            self._head = self._cursor
        else:
            temp = Node(value)

            self._cursor.next = temp
            temp.prev = self._cursor
            self._cursor = temp

        self._size += 1

    def insert(self, position: int, value: object) -> None:
        """Inserts a value at the given position of the list. The position must be less than or
        equal to the size of the list. If the position is equal to the size of the list, it 
        just adds the value to the end of the list.

        Args:
            position (int): The position to insert the value at.
            value (object): The value to insert at the given position.
        """
        assert position <= self._size, "Position must of less than or equal to the size of list."

        if position == self._size:
            self.add(value)
        elif position == 0:
            temp = Node(value)

            self._head.prev = temp
            temp.next = self._head

            self._head = temp
            self._size += 1
        else:
            i, current = 0, self._head

            while i < position and current:
                current = current.next
                i += 1

            temp = Node(value)
            current.prev.next = temp
            temp.next = current

            self._size += 1

    def remove(self, position: int) -> None:
        """Removes a node from the list at the given position. The position must be less than the
        size of the list.

        Args:
            position (int): The position of the node to remove.
        """
        assert position < self._size, "Position must be less than the list size."

        if position == 0:
            self._head = self._head.next

            if self._head:
                self._head.prev = None
        else:
            i, current = 0, self._head

            while current and i < position:
                current = current.next
                i += 1

            current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
        self._size -= 1

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def __str__(self) -> str:
        res = self.__class__.__name__ + '(['

        current = self._head
        while current:
            res += f", {str(current.value)}" if current != self._head else str(current.value)
            current = current.next

        res += '])'

        return res


if __name__ == "__main__":
    dl = DoublyLinkedList(2, 4)
    print(dl)

    dl.add(5)
    print(dl)

    dl.insert(2, -4)
    print(dl)

    dl.insert(4, 14)
    print(dl)

    dl.insert(0, 1)
    print(dl)

    dl.remove(5)
    print(dl)

    dl.remove(0)
    print(dl)

    dl.remove(1)
    print(dl)
