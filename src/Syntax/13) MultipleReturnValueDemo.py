def sort(number1, number2):
    if number1 < number2:
        return number1, number2
    else:
        return number2,number1

n1,n2 = sort(453,23)
print("n1 is", n1)
print("n2 is", n2)