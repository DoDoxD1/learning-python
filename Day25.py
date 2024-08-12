# with open("data.csv") as weather_data:
#     content = weather_data.read()
#     list = content.splitlines()
#     print(list)

# import csv
#
# # reading csv file
# with open("data.csv") as weather_data:
#     data = csv.reader(weather_data)
#
#     # creating a list of temperatures out of csv file
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas as pd

# data = pd.read_csv("data.csv")
# print(data)
# temp = data["temp"].to_list()
# print(sum(temp)//len(temp))
# print(data["temp"].max())

# print(data[data.temp == data.temp.max()])

data = pd.read_csv("squirrel.csv")
new_data = data["Primary Fur Color"].value_counts()
new_data.to_csv("new_file.csv")

# https://github.com/DoDoxD1/us-states-quiz-python
