def bubbleSort(array):
    length = len(array)
    for i in range(0, length):
        swapped = False
        for j in range(0, length - 1):
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]  # swap the elements
                swapped = True
        if not swapped:
            break
    return array


arr = [1, 5, 6, -9, 8, -96, 100, -65, 4, 5, 9]
sorted_array = bubbleSort(arr)
print(arr)
