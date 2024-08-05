# Challange 1 change marks into grades form dictionary
# def grade_strudents(student_scores):
#     student_grades = {}
#     for key in student_scores:
#         marks = student_scores[key]
#         if(marks>90):
#             student_grades[key] = "Outstanding"
#         elif(marks>80):
#             student_grades[key] = "Exceeds Exprectations"
#         elif(marks>70):
#             student_grades[key] = "Acceptable"
#         else:
#             student_grades[key] = "Fail"
#     return student_grades

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Darco": 74,
#     "Neville": 72,
# }
# print(grade_strudents(student_scores))

# cHALLANGE 2 add a data to the list of dictionary
# travel_log = []
# def add_new_data(country,visits,cities):
#     dictionary = {}
#     dictionary["country"] = country
#     dictionary["visits"] = visits
#     dictionary["cities"] = cities
#     travel_log.append(dictionary)
# add_new_data("Russia",2,["Moscow","Saint Petersburg"])
# print(travel_log)

from replit import clear

bids = {}
choice = "yes"
while choice == "yes":
    name = input("Enter your name: ")
    bid = int(input("What's your bid? "))
    bids[name] = bid
    choice = input("Are there any more people to bid(yes/no)? ").lower()
    clear()
max_bid = -1
name = ""
for key in bids:
    if(bids[key]>max_bid):
        max_bid = bids[key]
        name = key

print(f"{name} wins the bid at ${max_bid}")