from random import randint

def main():
    
    outputfile = open("numbers.txt", "w")
    for i in range(10):
        outputfile.write(str(randint(0,9))+" ")
    outputfile.close()
    
    infile = open("numbers.txt", "r")
    s = infile.read()
    numbers = [eval(x) for x in s.split()]
    for number in numbers:
        print(number, end =" ")
    infile.close()

main()
    