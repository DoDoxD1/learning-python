# Challange 1 find the average height of students
heights = input("Enter a list of student heights ").split()
sum = 0
count = 0 
for h in heights:
    h = int(h)
    sum += h
    count +=1
print(round(sum/count))