count = 0
candidate = 2

while count < 50:
    
    #Test candidate
    testNum = 2
    prime = True
    while testNum <= candidate /2:
        if candidate % testNum == 0:
            prime = False
            break
        testNum += 1
    
    if prime:
        count += 1
        print(candidate," ",end = '')
    
    candidate += 1
    