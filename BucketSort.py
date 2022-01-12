def InsertionSort(numbers):

    length = range(1,len(numbers)) 
    for i in (length):
        value_to_sort = numbers[i]
        while numbers[i-1] > value_to_sort and i >0:
            numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
            i -= 1

    return numbers 


def BucketSort(numbers):
    bucket = []
    slot = 100 # each bucket 10 slot
    for i in range(slot):
        bucket.append([]) # append array in bucket
    
    for j in numbers:
        index = int(slot * j)
        bucket[index].append(j) # assign index at each bucket, 1st bucket index 0, 2nd bucket index 1...
    
    for i in range(slot):
        bucket[i] = InsertionSort(bucket[i]) # sort elements in bucket
    
    k = 0
    for i in range(slot):
        for j in range(len(bucket[i])):
            numbers[k] = bucket[i][j] # takes elements from bucket at position i,j back to list
            k += 1

    return numbers

numbers = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print("Unsorted List: ",numbers)
print("Sorted List: ",BucketSort(numbers))