def insertionSort(array):
    length = len(array)
    for i in range(1, length):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j = j-1
    return array


arr = [1, 5, 6, -9, 8, -96, 100, -65, 4, 5, 9]
sorted_array = insertionSort(arr)
print(sorted_array)
