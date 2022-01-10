def Binarysearch(numbers, first, last, x):
    if last >= first:
        
        mid = int((first + last)//2)

        if numbers[mid] == x:
            return mid

        elif numbers[mid] > x:
            return Binarysearch(numbers, first, mid, x)
        
        else:
            return Binarysearch(numbers, mid, last, x)

    else:
        return -1
     


numbers = [1,2,3,4,5,6,7,8,9]
x = 4
search = Binarysearch(numbers, 0, len(numbers)-1, x)

if search != -1:
    print("number",x,"is found at index",search)

else:
    print("number",x,"is not present")