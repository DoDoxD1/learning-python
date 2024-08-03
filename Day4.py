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
names_str = input("Give me everybody's names, seperated by a comma: ")
names = names_str.split(", ")
# random_choice = names[random.randint(1,len(names)-1)]
# or
random_choice = random.choice(names)
print(f"{random_choice} is going to pay the bill.")