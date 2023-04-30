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

# remove header from each column
total_number.pop(0)
profit_losses.pop(0)

# calculate number of months in relevant list
total_months = int(len(total_number))

# convert profit/losses list to integer and float
profit_lossesint = [int(entry) for entry in profit_losses]
profit_lossesfloat = [float(entry) for entry in profit_losses]

# sum profit/losses list
profit_lossessum = sum(profit_lossesint)

# calculate net change
change_original = profit_lossesfloat[0]
change_final = profit_lossesfloat[-1]
change_net = change_final - change_original
change_numvalues = len(profit_lossesfloat) - 1
change_final = change_net / change_numvalues

# print title and dashed line
print("\nFinancial Analysis")
print("\n------------------------------\n")

# print total number of months in dataset
print(f"Total Months: {total_months}\n")

# print net total profit/losses with dollar symbol
print(f"Total: ${profit_lossessum}\n")

print(f"Average Change: ${change_final:.2f}\n")

