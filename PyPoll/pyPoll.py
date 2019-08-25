#import csv document
import csv
import os

csvpath = os.path.join("..", "PyPoll", "election_data.csv")

Candidates = []
Candidate_votes = {}
total = 0
percents = 0
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
        
    total = 1048575
    for row in csvreader:
        Candidate_Name = row[2]
        if Candidate_Name not in Candidates:
            Candidates.append(Candidate_Name)
            Candidate_votes[Candidate_Name]= 0
           