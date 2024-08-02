# Datatypes
# String ("Hello")
# subscript/indexing of string
# Integer (1, 2, 1000)
# Float (1.23, 3.14)
# Boolean (t]True, False)

# Challange 1 Add the digits of a two digit number.
# num = int(input("Enter a two digit number: "))
# tens_place = num//10
# ones_place = num - tens_place*10
# print("The sum of the digits  is: ",(ones_place+tens_place))

# Challange 2 BMI Calculator
# height = float(input("What is your height in m: "))
# weight = float(input("What is your weight in kg: "))
# print("Your BMI: ",int(weight/height**2))

# Challange 3 Calculate number of weeks left in your life
age = int(input("What is your age? "))
years_left = 90-age
months_left = years_left*12
weeks_left = years_left*52
days_left = years_left*365
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")