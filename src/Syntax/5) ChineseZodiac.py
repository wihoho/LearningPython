year = eval(input("Enter a year?"))
zodiacYear = year % 12

if zodiacYear == 0:
    print("monkey")
elif zodiacYear == 1:
    print("rooster")
else:
    print("nothing")