import csv
import os

csvpath = os.path.join("..", "PyPoll", "election_data.csv")

# Open and read csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
cand = []
    for filter in csvreader:
        cand.append(str(row[2]))
        x = cand.append(row[2])
print (x)

