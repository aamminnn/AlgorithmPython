def MergeSort(numbers):
    if len(numbers) > 1:

        mid = len(numbers)//2

        left = numbers[:mid]
        right = numbers[mid:]

        MergeSort(left)
        MergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1

def printSorted(numbers):
    sorted = []
    for i in range(len(numbers)):
        sorted.append(numbers[i])
    print("Sorted List: ",sorted)


numbers = [21,57,9,46,35,13]
print("Unsorted list: ",numbers)
MergeSort(numbers)
printSorted(numbers)
