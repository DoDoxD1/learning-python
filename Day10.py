# Challange1 print number of days
# from Day3 import isLeap

# def days_in_month(year,month):
#     months = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if(month == 2 and isLeap(year)): return 29
#     else:  return months[month-1]
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))

# print(days_in_month(year,month))

#project calculator
from art import logo_calculator
def operate(a,b,op):
    if(op=="+"):
        return a+b
    elif(op=="-"):
        return a-b
    elif(op=="*"):
        return a*b
    elif(op=="/"):
        return a/b
    else:
        return 0
    
def calculate():
    a = int(input("What's the first number?: "))
    print("+\n-\n*\n/")
    op = input("Pick an operation: ")
    b = int(input("What's the next number?: "))
    res = operate(a,b,op)
    print(f"The result of {a} {op} {b} = {res}")
    while input("Do you want to continue? (y/n): ") == "y":
        op = input("Pick an operation: ")
        b = int(input("What's the next number?: "))
        a = res
        res = operate(a,b,op)
        print(f"The result of {a} {op} {b} = {res}")
    calculate()

print(logo_calculator)
calculate()