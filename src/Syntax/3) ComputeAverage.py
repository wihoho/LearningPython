#Prompt the user to enter three numbers
#Simultaneous Assignment
#Note that the input numbers should be separated by commas
#For example: input: 1,2,3  output: 2.0
number1, number2, number3 = eval(input("Enter the three numbers: "))

#Compute the average
average = (number1 + number2 + number3) / 3

#Display the result
print("The average of these three numbers is",average)
