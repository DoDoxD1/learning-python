# Challange 1 find the average height of students
# heights = input("Enter a list of student heights ").split()
# sum = 0
# count = 0 
# for h in heights:
#     h = int(h)
#     sum += h
#     count +=1
# print(round(sum/count))

# Challange 2 find the highest marks of students
# marks_list = input("Enter a list of student marks ").split()
# max_marks=-1
# for marks in marks_list:
#     marks = int(marks)
#     if(marks>max_marks): max_marks = marks
# print(max_marks)

# Challange 3 calculate sum of even numbers from 1to100
# sum = 0
# for n in range(2,101,2):
#     sum += n
# print(sum)

# Challange 4 fizzbzz from 1to100
# for n in range(1,101):
#     if(n%15==0): print("FizzBuzz")
#     elif(n%3==0): print("Fizz")
#     elif(n%5==0): print("Buzz")
#     else: print(n)

# Project password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
n_letters= int(input("How many letters would you like in your password?\n")) 
n_symbols = int(input(f"How many symbols would you like?\n"))
n_numbers = int(input(f"How many numbers would you like?\n"))
password = ""

for i in range(0,n_letters):
    if(n_numbers!=0): 
        password += numbers[random.randint(0,len(numbers)-1)]
        n_numbers -= 1
    elif(n_symbols!=0): 
        password += symbols[random.randint(0,len(symbols)-1)]
        n_symbols -= 1
    else: password += letters[random.randint(0,len(letters)-1)]
password = ''.join(random.sample(password,len(password)))
print(password)