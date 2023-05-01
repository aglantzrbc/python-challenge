# import module for creating file paths across operating systems for this project
import os

# import module for reading csv files
import csv

# get data from correct path
pybankpath = os.path.join("python-challenge", "PyBank", "Resources", "budget_data.csv")

# read csv resource file for this project
with open(pybankpath) as pybankfile:
    
    # specify delimiter and variable that holds contents of file
    pybankreader = csv.reader(pybankfile)

    # exclude header row
    header = next(pybankreader)


    # initialize all variables
    changes = []
    count_rows = 0
    total_revenue = 0
    prev_revenue = 0
    greatest_increase = {"date": "", "amount": float("-inf")}
    greatest_decrease = {"date": "", "amount": float("inf")}


    # iterate through datafile
    for row in pybankreader:
        date = row[0]
        revenue = int(row[1])
        count_rows += 1
        total_revenue += revenue

        if prev_revenue != 0:
            change = revenue - prev_revenue
            changes.append(change)

            # calculate greatest increase in revenue
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change

            # calculate greatest decrease in revenue
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change
        
        prev_revenue = revenue

# Calculate average revenue change
avg_revenue = sum(changes) / len(changes)

# Print header and line
print(f"\nFinancial Analysis\n")
print(f"----------------------------\n")

# Print total months sum
print(f"Total Months: {count_rows}\n")

# Print total revenue sum
print(f"Total: ${total_revenue}\n")

# Print net change in revenue over time period
print(f"Average Change: ${avg_revenue:.2f}\n")

# Print greatest revenue increase and greatest revenue decrease with dates
print(f"Greatest Increase in Revenue: {greatest_increase['date']} (${greatest_increase['amount']})\n")
print(f"Greatest Decrease in Revenue: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")
    
