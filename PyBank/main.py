# import module for creating file paths across operating systems for this project
import os
print(os.getcwd())

# import module for reading csv files
import csv

csvpath = os.path.join("python-challenge", "PyBank", "Resources", "budget_data.csv")

# read csv resource file for this project
with open(csvpath) as csvfile:

    # specify delimiter and variable that holds contents of file
    csvreader = csv.reader(csvfile)

    print(csvreader)