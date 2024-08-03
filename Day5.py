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
marks_list = input("Enter a list of student heights ").split()
max_marks=-1
for marks in marks_list:
    marks = int(marks)
    if(marks>max_marks): max_marks = marks
print(max_marks)