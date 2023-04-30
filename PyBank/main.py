# import module for creating file paths across operating systems for this project
import os

# import module for reading csv files
import csv

# get data from correct path
pybankpath = os.path.join("python-challenge", "PyBank", "Resources", "budget_data.csv")


# initialize variables
profloss_changes = []
count_rows = 0
profloss_revenue = 0
profloss_prev = 0
greatest_profit = {"date": "", "amount": float("-inf")}
greatest_loss = {"date": "", "amount": float("inf")}

# read csv resource file for this project
with open(pybankpath) as pybankfile:
    
    # specify delimiter and variable that holds contents of file
    pybankreader = csv.reader(pybankfile)

    # exclude header row
    header = next(pybankreader)

# iterate through datafile
    for row in pybankreader:
        date = row[0]
        amount = int(row[1])
        count_rows += 1
        profloss_revenue += amount

        if profloss_prev != 0:
            change = amount - profloss_prev
            profloss_changes.append(change)

            # calculate greatest increase in revenue
            if change > greatest_profit["amount"]:
                greatest_profit["date"] = date
                greatest_profit["amount"] = change

            # calculate greatest decrease in revenue
            if change < greatest_loss["amount"]:
                greatest_loss["date"] = date
                greatest_loss["amount"] = change
        
        profloss_prev = profloss_revenue

# average revenue change
avg_revenue = sum(profloss_changes) / len(profloss_changes)

# print title and dashed line
print("\nFinancial Analysis\n")
print("------------------------------\n")

# print total number of months in dataset
print(f"Total Months: {count_rows}\n")

# print net total profit/losses with dollar symbol
print(f"Total: ${profloss_revenue}\n")

# print average change with two decimal spaces
print(f"Average Change: ${avg_revenue}\n")

# print greatest increase in profits date and (amount)
print(f"Greatest Increase in Profits: {greatest_profit[date]} (${greatest_profit[amount]})\n")

# print greatest decrease in profits date and (amount)
print(f"Greatest Decrease in Profits: {greatest_loss[date]} (${greatest_loss[amount]})\n")
