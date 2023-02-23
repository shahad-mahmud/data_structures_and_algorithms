import math


class DynamicArray(object):
    def __init__(self, *objects):
        if not objects:
            # Initializing an empty list. Set initial capacity to 2
            self._list = [None] * 2
            self._length = 0
            self._capacity = 2
        else:
            # Initialize the list using the given objects. At first calculate the number of
            # objects. Then calculate the capacity. We increase the capacity in power of 2.
            # So, to calculate the capacity, we determine the number of bits required to
            # represent the number of objects using 2 based log. Then add 1 to it and create
            # and empty array. Finally assign the objects to the newly created array.
            self._length = 0

            for _ in objects:
                self._length += 1

            self._capacity = 2 ** (math.ceil(math.log(self._length, 2)) + 1)
            self._list = [None] * self._capacity

            for i, obj in enumerate(objects):
                self._list[i] = obj

    def add(self, obj: object):
        # Add an object at the end of the array.
        if self._length + 1 > self._capacity:
            temp = [None] * (self._capacity * 2)
            self._capacity *= 2

            for i in range(self._length):
                temp[i] = self._list[i]

            self._list = temp

        self._list[self._length] = obj
        self._length += 1

    def insert(self, obj: object, index: int):
        # Insert an object at a given index.
        assert isinstance(
            index, int) and index >= 0, "Index must be a positive integer."
        assert index <= self._length, "Index must be less than or equal to array size"

        if self._length + 1 > self._capacity:
            # No space left. Grow the array.
            temp = [None] * (self._capacity * 2)
            self._capacity *= 2

            for i in range(self._length):
                temp[i] = self._list[i]

            self._list = temp

        # Shift each element to right until the `index` to make room for the `obj`.
        for i in range(self._length-1, index-1, -1):
            self._list[i+1] = self._list[i]

        self._list[index] = obj
        self._length += 1

    def remove(self, index: int):
        # remove an object from a given index
        assert isinstance(
            index, int) and index >= 0, "Index must be a positive integer."
        assert index < self._length, "Index must be less than array size"

        for i in range(index, self._length-1):
            self._list[i] = self._list[i+1]
        self._list[self._length-1] = None

        self._length -= 1

        if self._length <= self._capacity // 2:
            self._capacity = self._capacity // 2
            self._list = [self._list[i] for i in range(self._capacity)]

    def pop(self) -> object:
        # remove from the end of array
        assert self._length > 0
        obj = self._list[self._length - 1]

        self._list[self._length - 1] = None
        self._length -= 1

        if self._length <= self._capacity // 2:
            self._capacity = self._capacity // 2
            self._list = [self._list[i] for i in range(self._capacity)]

        return obj

    def size(self):
        # get the size of the array
        return self._length

    def __str__(self):
        result = '['
        result += ', '.join([str(self._list[i])
                            for i in range(self._length)]) + ']'

        return result


if __name__ == '__main__':
    l = DynamicArray(2, 3, 4)
    l.add(5)
    l.add(6)
    l.add(7)
    l.add(8)
    l.add(9)
    print(l)
    print(l.size())

    l.add(10)
    print(l)
    print(l.size())

    l.pop()
    print(l)

    l.remove(2)
    print(l)

    l.insert(-4, 1)
    print(l)

    l.insert(20, 8)
    print(l)
