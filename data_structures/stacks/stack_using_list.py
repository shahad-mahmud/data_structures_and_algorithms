"""
This script contains the implementation of stack data structure using array or list. This implementation contains the basic functionalities
including push, pop, peek, get size, check if empty.
"""


class Stack(object):
    def __init__(self, value: object = None):
        if value:
            self._list = [value]
        else:
            self._list = []

        self._size = 1 if value else 0

    def push(self, value: object) -> None:
        """Push a value into the to of the stack.

        Args:
            value (object): The value to push.
        """
        self._list.append(value)

        self._size += 1

    def pop(self):
        """Pop the last or top value from the stack. Raises an exception if the stack is empty."""

        assert not self.is_empty(), "Stack is empty. Nothing to pop."

        del self._list[-1]
        self._size -= 1

    def peek(self):
        """Peek the stack and return the top or last element from the stack.

        Returns:
            object: The top or last element of the stack
        """
        assert not self.is_empty(), "Stack is empty. Nothing to peek."

        return self._list[-1]

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def __str__(self) -> str:
        res = self.__class__.__name__ + '['

        for i, value in enumerate(self._list):
            res += str(value) if i == 0 else f", {value}"

        res += ']'

        return res


if __name__ == "__main__":
    s = Stack(2)

    s.push(7)
    s.push(6)

    print(s)

    print(s.peek())
    s.pop()

    print(s.peek())
    s.pop()

    print(s.peek())
    s.pop()

    print(s.peek())  # will raise error
