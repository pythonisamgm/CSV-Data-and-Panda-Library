with open("./weather_data.csv") as data_file:
    data = data_file.read().splitlines()
#    print (data)
import csv

with open ("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print (temperatures)

import pandas

# saca la info de una columna
data = pandas.read_csv("weather_data.csv")
print(type(data))
print (data)
temp = (data["temp"])

#hace la media de una columna
average_temp= sum(temp)/(len(temp))
#print (round(average_temp, 2))
print(data["temp"].mean())
print (temp.max())

#saca el máximo numero en una columna/lista
max_temp = 0
for individual_temp in temp:
    if individual_temp > max_temp:
        max_temp = individual_temp
print (max_temp)

hottest_day = data[data.temp == data.temp.max()]
print (hottest_day)


#particular row's temperature o condition
monday = data[data.day == "Monday"]
print (monday.condition)

monday_temp = monday.temp[0]
monday_fahrenheit = (monday_temp * 9/5) + 32
print (monday_fahrenheit)


#create a dataframe from scratch; convert ir to csv
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data2 = pandas.DataFrame(data_dict)
data2.to_csv ("path_to_save_it.csv")


#loop throgh rows of a data frame ITERROWS

student_dict ={
    "student": ["Angela", "James", "Lily"]
    "score": [56, 76, 98]
}

student_df=pandas.DataFrame(student_dict)

for (index, row) in student_df.iterrows():
    print(index)
    print(row)
    print(row.student)
    if row.student =="Angela":
        print(row.score)


