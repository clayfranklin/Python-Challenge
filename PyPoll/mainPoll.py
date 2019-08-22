import csv
import os

csvpath = os.path.join("..", "PyPoll", "election_data.csv")

# Open and read csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

print(row[1])