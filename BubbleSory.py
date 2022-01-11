def BubbleSort(numbers):

    n = len(numbers)
    sorted = []

    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
    for i in range(n):
        sorted.append(numbers[i])
    print("Sorted List: ",sorted)


numbers = [21,57,9,46,35,13]
print("original list: ",numbers)
BubbleSort(numbers)