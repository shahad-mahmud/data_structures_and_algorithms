def merge(A, i, l, m):
    size1 = m - i + 1
    size2 = l - m

    list1 = A[i:m + 1]
    list2 = A[m + 1:l + 1]

    k = 0
    j = 0
    index = i
    while k < size1 and j < size2:
        if list1[k] < list2[j]:
            A[index] = list1[k]
            k += 1
        else:
            A[index] = list2[j]
            j += 1
        index += 1

    while k < size1:
        A[index] = list1[k]
        k += 1
        index += 1

    while j < size2:
        A[index] = list2[j]
        j += 1
        index += 1
    return A


def mergeSort(A, i, l):
    if i >= l:
        return A
    m = int((i + l) / 2)
    mergeSort(A, i, m)
    mergeSort(A, m + 1, l)
    merge(A, i, l, m)
    return A


arr = [50, 12, 65, -5, 10, -8, 0, 4, 556, -234, 4, 4, 234, -324]
sorted_array = mergeSort(arr, 0, len(arr) - 1)
print(sorted_array)
