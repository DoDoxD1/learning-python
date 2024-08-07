#Project guess the number
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

number = random.randint(1,100)

if(difficulty=='easy'): attempts = 10   
else : attempts = 5
print(f"You've got {attempts} attempts. Good Luck!")

while (attempts>0):
    attempts -= 1
    guess = int(input("Guess a number: "))
    if(guess == number):
        print(f"You won! the number was {guess}")
        break
    if(attempts != 0):
        if(guess<number):
            print("Too low! guess higher")
        else:
            print("Too high! guess lower")
        print(f"You have {attempts} attempts left.")
        
if (attempts == 0): print("You lost! try again")