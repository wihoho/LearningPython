import random

number = random.randint(0,100)
print("Guess a magic number between 0 and 100")

guess = -1
while guess != number:
    guess = eval(input("Enter your guess: "))
    
    if guess == number:
        print("Yes, the number is", guess)
    elif guess > number:
        print("Your number is too high")
    else:
        print("Your number is too low")