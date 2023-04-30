# import module for creating file paths across operating systems for this project
import os

# import module for reading csv files
import csv

# create lists to store data
total_number = []
profit_losses = []

# get data from correct path
pybankpath = os.path.join("python-challenge", "PyBank", "Resources", "budget_data.csv")

# read csv resource file for this project
with open(pybankpath) as pybankfile:
    
    # specify delimiter and variable that holds contents of file
    pybankreader = csv.reader(pybankfile)

    # add data as lists to variables
    for row in pybankreader:
        total_number.append(row[0])
        profit_losses.append(row[1])

# calculate number of months in relevant list
num_months = int(len(total_number) - 1)

# print title and dashed line with proper line spacing
print("\nFinancial Analysis")
print("\n------------------------------\n")

# print total number of months in dataset
print(f"Total Months: {num_months}")


