import math

def Jumpsearch(numbers, x):
    n = len(numbers) # array length
    m = math.sqrt(n) # steps of block
    first = 0 # first index of block

    while numbers[int(min(m,n)-1)] < x:
        first = m
        m += m
        if first >= n:
            return -1
    
    while numbers[int(first)] < x:
        first += 1
        if first == min(m,n):
            return -1
    
    if numbers[int(first)] == x:
        return first
    
    else:
        return -1



numbers = [1,3,5,9,13,18,21,26,27,31,45,66,78]
x = 27

search = Jumpsearch(numbers, x)
if (search != -1):
    print(x, "is found at index", int(search))

else:
    print(x, "is not found")