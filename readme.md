# Weather Data Analysis

This Python script demonstrates various operations on weather data using CSV reading, list manipulations, and the pandas library for data analysis. It includes tasks such as reading data from a CSV file, calculating average temperatures, finding maximum temperatures, and converting temperatures.

## Installation

1. Clone the repository or download the script files.
2. Make sure you have Python installed on your system. This script requires Python 3.x.
3. Install the necessary Python packages using pip:
    ```sh
    pip install pandas
    ```

## Usage

1. Ensure you have a CSV file named `weather_data.csv` in the same directory as the script. The CSV should have the following format:
    ```
    day,temp,condition
    Monday,12,Sunny
    Tuesday,14,Cloudy
    ...
    ```

2. Run the script:
    ```sh
    python weather_data_analysis.py
    ```

## Script Details

The script performs the following operations:

1. **Reading CSV Data without Pandas:**
    ```python
    with open("./weather_data.csv") as data_file:
        data = data_file.read().splitlines()
    ```

2. **Reading CSV Data using csv.reader:**
    ```python
    import csv

    with open("weather_data.csv") as data_file:
        data = csv.reader(data_file)
        temperatures = []
        for row in data:
            if row[1] != "temp":
                temperatures.append(int(row[1]))
        print(temperatures)
    ```

3. **Reading CSV Data using Pandas:**
    ```python
    import pandas

    data = pandas.read_csv("weather_data.csv")
    print(type(data))
    print(data)
    temp = data["temp"]
    ```

4. **Calculating Average Temperature:**
    ```python
    average_temp = sum(temp) / len(temp)
    print(data["temp"].mean())
    print(temp.max())
    ```

5. **Finding Maximum Temperature:**
    ```python
    max_temp = 0
    for individual_temp in temp:
        if individual_temp > max_temp:
            max_temp = individual_temp
    print(max_temp)

    hottest_day = data[data.temp == data.temp.max()]
    print(hottest_day)
    ```

6. **Extracting Specific Row Data:**
    ```python
    monday = data[data.day == "Monday"]
    print(monday.condition)

    monday_temp = monday.temp.iloc[0]
    monday_fahrenheit = (monday_temp * 9/5) + 32
    print(monday_fahrenheit)
    ```

7. **Creating a DataFrame from Scratch and Saving to CSV:**
    ```python
    data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }
    data2 = pandas.DataFrame(data_dict)
    data2.to_csv("path_to_save_it.csv", index=False)
    ```

8. **Iterating through Rows of a DataFrame:**
    ```python
    student_dict = {
        "student": ["Angela", "James", "Lily"],
        "score": [56, 76, 98]
    }

    student_df = pandas.DataFrame(student_dict)

    for (index, row) in student_df.iterrows():
        print(index)
        print(row)
        print(row.student)
        if row.student == "Angela":
            print(row.score)
    ```

## Example

Here is an example of how the script works with the provided `weather_data.csv`:

- It calculates the average temperature:
    ```
    13.0
    ```

- It finds the maximum temperature:
    ```
    14
    ```

- It extracts the condition for Monday:
    ```
    Sunny
    ```

- It converts Monday's temperature to Fahrenheit:
    ```
    53.6
    ```
