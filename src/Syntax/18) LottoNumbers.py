isCovered = 99 * [False]
endOfInput = False

while not endOfInput:
    s = input("Enter a line numbers seperated by spaces: ")
    items = s.split(sep = " ")
    lst = [eval(x) for x in items]
    
    for number in lst:
        if number == 0:
            endOfInput = True
        else:
            isCovered[number - 1] = True

allCovered = True
for i in range(100):
    if not isCovered[i]:
        allCovered = False
        break

if allCovered:
    print("The tickets cover all number")
else:
    print("The tickets do not cover all numbers")