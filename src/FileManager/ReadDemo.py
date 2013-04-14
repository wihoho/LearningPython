def main():
    infile = open("President.txt","r")
    print("1) Using read(): ")
    print(infile.read())
    infile.close()
    
    infile = open("President.txt","r")
    print("\n2) Using read(number): ")
    s1 = infile.read(4)
    print(s1)
    s2 = infile.read(10)
    print(s2)
    infile.close()
    
    infile = open("President.txt","r")
    print("\n3) Using readline(): ")
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    print(repr(line1))
    print(repr(line2))
    print(repr(line3))
    print(repr(line4))    
    infile.close();
    
    infile = open("President.txt","r")
    print("\n4) Using readlines(): ")
    line = infile.readlines()
    print(line)
    
    
main()