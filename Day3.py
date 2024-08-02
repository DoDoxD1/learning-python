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
year = int(input("Enter the year: "))
if(year%400==0 or (year%4==0 and year%100!=0)):
    print("It's a leap year")
else:
    print("It's not leap year")

