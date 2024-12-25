def quickSort(array, lowIndex, highIndex):
    if lowIndex < highIndex:
        pivot = partition(array, lowIndex, highIndex)
        quickSort(array, lowIndex, pivot - 1)
        quickSort(array, pivot + 1, highIndex)


def partition(array, lowIndex, highIndex):
    partpivot = array[highIndex]
    i = lowIndex - 1

    for j in range(lowIndex, highIndex):
        if array[j] <= partpivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[highIndex]) = (array[highIndex], array[i + 1])
    return i + 1


data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)
print(data)

