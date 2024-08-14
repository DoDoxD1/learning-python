# # list comprehensions
# data = range(1, 5)
# new = [n*2 for n in data]
# print(new)

# # challenge 1
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [x*x for x in numbers]
# print(squared_numbers)

# # challenge 2
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [x for x in numbers if x % 2 == 0]
# print(result)

# dictionary comprehension
# # challenge 3
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words = sentence.split()
# result = {x: len(x) for x in words}
# print(result)

# # challenge 4
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {k: (v*9/5)+32 for (k, v) in weather_c.items()}
# print(weather_f)

# project
# https://github.com/DoDoxD1/nato-phonetic-python