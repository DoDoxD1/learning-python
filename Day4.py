#Day 4 Randomisation
import random
# num = random.randint(1,10)
# num2 = random.random()*5
# print(num)
# print(num2)

# Challange 1 Head or tails
# num = random.randint(0,1)
# if(num==1): print("Head")
# else: print("Tails")

# Challange 2 banker roulette
# names_str = input("Give me everybody's names, seperated by a comma: ")
# names = names_str.split(", ")
# # random_choice = names[random.randint(1,len(names)-1)]
# # or
# random_choice = random.choice(names)
# print(f"{random_choice} is going to pay the bill.")

# Challange 3 mark the treasure
# row1 = ["⬜","⬜","⬜"]
# row2 = ["⬜","⬜","⬜"]
# row3 = ["⬜","⬜","⬜"]
# map = [row1,row2,row3]
# col_row = input("Where do you want to put the treasure? ")
# col = int(col_row[0])-1
# row = int(col_row[1])-1
# map[row][col] = " X"
# print(f"{map[0]}\n{map[1]}\n{map[2]}")

# Project rock, paper, scissors
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
rpc = [rock,paper,scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
print(rpc[user])
computer = random.randint(0,2)
print(f"Computer chose:\n{rpc[computer]}")
if((user==0 and computer==2) or (user==2 and computer==1) or (user==1 and computer==0)):
    print("You win!")
elif((user==2 and computer==0) or (user==1 and computer==2) or (user==0 and computer==1)):
    print("You loose.")
else:
    print("It's a draw.")