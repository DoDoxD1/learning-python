#Challange 1 ODD or EVEN
# num = int(input("Enter a number: "))
# if(num%2==0):
#     print("The number is even.")
# else:
#     print("The number is odd.")

#Challange 2 BMI Interpretation
# height = float(input("What is your height in m: "))
# weight = float(input("What is your weight in kg: "))
# bmi = int(weight/height**2)
# msg = ""
# if(bmi<=18.5):
#     msg = "underweight"
# elif(bmi<=25):
#     msg = "at normal weight"
# elif(bmi<=30):
#     msg = "slightly overweight"
# elif(bmi<=35):
#     msg = "obese"
# else:
#     msg = "very obese"
# print(f"Your BMI is {bmi}, you are {msg}")

#Challange 3 check for leap year
def isLeap(year):
    if(year%400==0 or (year%4==0 and year%100!=0)):
        return True
    else:
        return False

#Challange 4 Pizza order bill
# print("Welcome to my pizza shop!")
# size = input("What is the size of pizza you want? S, M, or L ")
# pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0
# if(size == "S"): bill += 15
# elif(size == "M"): bill += 20
# else: bill += 25
# if(pepperoni == "Y"): bill += 2
# if(extra_cheese == "Y"): bill += 3
# print(f"Your bill is {bill}, Thank you for your order!")

#Challange 5 Love calculator
# name1 = input("Enter your name: ").lower()
# name2 = input("Enter their name: ").lower()
# name = name1+name2
# tens_place = name.count("t")+name.count("r")+name.count("u")+name.count("e")
# ones_place = name.count("l")+name.count("o")+name.count("v")+name.count("e")
# love = int(str(tens_place)+str(ones_place))
# msg = ""
# if(love>90 or love<10): msg = "you go together like coke and mentos"
# elif(love>40 and love<50): msg = "you are alright together"
# print(f"Your love is {love} out of 100, {msg}")

#Project Day 3 Treasure hunt
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 
# left_right = input("Left of right? ").lower()
# if(left_right=="left"):
#     swim = input("Swim or wait for the wait? ").lower()
#     if(swim=="wait"):
#         door = input("Which door? Red, Blue or Yellow ")
#         if(door=="yellow"):
#             print("You win")
#         elif(door=="red"):
#             print("The floore is lava, Game Over!")
#         else:
#             print("Game Over!")
#     else:
#         print("Eaten by crocodiles, Game Over!")
# else:
#     print("You fell into the pothole, Game Over!")