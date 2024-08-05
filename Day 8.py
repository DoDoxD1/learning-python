# Challange 1 Paint the wall
# def paintWall(h,w,coverage):
#     area = h*w
#     number_of_cans = area/coverage
#     print(f"You will need {round(number_of_cans)} to paint the wall.")

# height = int(input("Enter the height of the wall: "))
# width = int(input("Enter the width of the wall: "))
# coverage = 5
# paintWall(height,width,coverage)

# Challange 2 Prime number check
# def checkPrime(number):
#     isPrime = True
#     for i in range(2,number//2):
#         if number%i == 0:
#             isPrime = False
#             break
#     return isPrime

# num = int(input("Enter a number: "))
# if(checkPrime(num)):
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

# Project ceaser cipher
from art import logo
def encode(str,n):
    l = list(str.encode('ascii'))
    l = [x+n for x in l]
    encoded = "".join(chr(x) for x in l)
    return encoded
def decode(str,n):
    l = list(str.encode('ascii'))
    l = [x-n for x in l]
    decoded = "".join(chr(x) for x in l)
    return decoded

print(logo)
choice = input("Choose encode or decode: ")
str = input("Enter the message\n")
n = int(input("Enter the number to shift\n"))
if(choice == "encode"): print(encode(str,n))
elif(choice == "decode"): print(decode(str,n))
else: print("Wrong choice")