def SelectionSort(numbers):
    last = len(numbers)
    sorted = []
    for i in range(last): 
        low = i
        for j in range(i+1, last):
            if numbers[low] > numbers[j]:
                low = j
        
        # swap low element with first
        numbers[i], numbers[low] = numbers[low], numbers[i]
    
    for i in range(last):
        sorted.append(numbers[i])

    print("Sorted List: ",sorted)
    





numbers = [21,57,9,46,35,13]
print("original list: ",numbers)
SelectionSort(numbers)

