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
row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
map = [row1,row2,row3]
col_row = input("Where do you want to put the treasure? ")
col = int(col_row[0])-1
row = int(col_row[1])-1
map[row][col] = " X"
print(f"{map[0]}\n{map[1]}\n{map[2]}")