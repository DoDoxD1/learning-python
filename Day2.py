# Datatypes
# String ("Hello")
# subscript/indexing of string
# Integer (1, 2, 1000)
# Float (1.23, 3.14)
# Boolean (t]True, False)

# Challange 1
num = int(input("Enter a two digit number: "))
tens_place = num//10
ones_place = num - tens_place*10
print("The sum of the digits  is: ",(ones_place+tens_place))