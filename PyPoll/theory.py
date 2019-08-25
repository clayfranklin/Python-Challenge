import csv
import os

csvpath = os.path.join("..", "PyBank", "election_data.csv")

# Open and read csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(cvsreader)
    votes = [""]
    Kahn = 0
    for row in cvsreader:
        votes.append(row[1])
        x = votes
    if row in cvsreader is "Kahn"
        Kahn = 1
print(Kahn_votes)