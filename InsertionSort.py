# set index i
# if arr[i+1] < arr[i]
# swap arr[i],arr[i+1]
# i+=1

def InsertionSort(numbers):

    length = range(1,len(numbers)) 
    for i in (length):
        value_to_sort = numbers[i]
        while numbers[i-1] > value_to_sort and i >0:
            numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
            i -= 1

    return numbers 





numbers = [21,57,9,46,35,13]
print("Unsorted List: ", numbers)
print("Sorted List: ",InsertionSort(numbers))