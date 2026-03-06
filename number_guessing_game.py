import random

print("Welcome to the number guessing game.Please choose a lower and upper bound")

low = int(input("Enter the lower bound: "))

upper = int(input("Enter the upper bound: "))

max_attempts = 6

attempts = 0

number = random.randint(low,upper)

while attempts < max_attempts :
    guessed_number = int(input("Your guess: "))
    attempts += 1
    print("Your attempt number :", attempts)
    if guessed_number < low or guessed_number > upper :
        print("The numbers you guessed are not valid!")
        attempts -=1
    elif  guessed_number == number:
        print("Congratulations!")
        break
    elif guessed_number < number:
        print("Try Again! You guessed too small.")
    elif guessed_number > number:
        print("Try Again! You guessed too high.")
        
if attempts == max_attempts and guessed_number != number:
    print("Game over! The number was:", number)