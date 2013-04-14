def insertSort(lst):
    for i in range(1, len(lst)):
        currentElement = lst[i]
        k = i -1
        while k >=0 and lst[k] > currentElement:
            lst[k+1] = lst[k]
            k -= 1
        
        lst[k+1] = currentElement

list = [1,6,3,4,6,2,9]
print(list)
insertSort(list)
print(list)