def Linearsearch(numbers, x):
    first = 0
    last = len(numbers)
    for i in range(first, last):
        if numbers[i] == x:
            return i
    return -1

numbers = [1,2,3,4,5,6,7,8,9]
x = 8

search = Linearsearch(numbers,x)
if (search != -1):
    print("number", x, "is found at index", search)

else:
    print(x, "is not found")
