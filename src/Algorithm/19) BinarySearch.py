def binarySearch(lst, key):
    low = 0
    high = len(lst) - 1
    
    while high >= low:
        mid = (high + low) // 2
        if key < lst[mid]:
            high = mid -1
        elif key > lst[mid]:
            low = mid + 1
        else:
            return mid
    
    return -low - 1

lst = [2,4,7,10,11,45,50,59,60,66,69,70,79]
i = binarySearch(lst,2)
j = binarySearch(lst,11)
k = binarySearch(lst,12)
l = binarySearch(lst,1)
m = binarySearch(lst,3)

print(i)
print(j)
print(k)
print(l)
print(m)