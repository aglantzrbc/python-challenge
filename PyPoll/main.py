# import module for creating file paths across operating systems for this project
import os

# import module for reading csv files
import csv

# get data from correct path
pypollpath = os.path.join("python-challenge", "PyPoll", "Resources", "election_data.csv")

# initialize variables
candidates_list = []
counter = 0
stockham_counter = 0
degette_counter = 0
doane_counter = 0

# read csv resource file for this project
with open(pypollpath) as pypollfile:
    
    # specify delimiter and variable that holds contents of file
    pypollreader = csv.reader(pypollfile, delimiter=",")

    # exclude header row
    header = next(pypollreader)

    for row in pypollreader:
        ballot_id = row[0]
        county = row[1]
        candidate = row[2]
        candidates_list.append(candidate)
        counter +=1

# create list of candidates    
my_set = set(candidates_list)
my_new_list = list(my_set)
my_new_list.sort()
print(my_new_list)

# create votes counts by candidate
for row2 in candidates_list:
    if row2 == my_new_list[0]:
        stockham_counter += 1
    elif row2 == my_new_list[1]:
        degette_counter += 1
    else:
        doane_counter += 1

# percentage of votes counts by candidate
stockham_percentage = (stockham_counter / counter) * 100
degette_percentage = (degette_counter / counter) * 100
doane_percentage = (doane_counter / counter) * 100


# print title and dashed line
print("\nElection Results\n")

print("------------------------------\n")

# print total number of votes and line
print(f"Total Votes: {counter}\n")
print("------------------------------\n")

# print votes and percentage by candidate
print(f"{my_new_list[0]}: {stockham_percentage}% ({stockham_counter})")