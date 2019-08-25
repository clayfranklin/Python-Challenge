#import csv document
import csv
import os
from collections import Counter

csvpath = os.path.join("..", "PyPoll", "election_data.csv")

Candidates = []
Candidate_Dict = {}
Candidate_votes = {}
Khan_votes = 0
Khan = "Khan"
total = 0
winner = 0
percentage = 0

print("Election Results")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
        
    print("-------------------------")
    for row in csvreader:
        total += 1
print("Total Votes: " + (str(total)))

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
        
    print("-------------------------")
    for row in csvreader:
        Candidate_Name = row[2]
        Candidates.append(Candidate_Name)
    Candidate_Dict = dict(Counter(Candidates))

Khan_percent =Candidate_Dict["Khan"]*100/total
Khan_percent = round(Khan_percent)
K_dogPercent = str(Khan_percent)
Correy_percent = Candidate_Dict["Correy"]*100/total
Li_percent =Candidate_Dict["Li"]*100/total
Otooly_percent = Candidate_Dict["O'Tooley"]*100/total

#print("Khan : " + str(Khan_percent) + "%", 
#for i in Candidate_Dict: 
    #print(i, Candidate_Dict[i])

print("Khan : " , K_dogPercent , str(Candidate_Dict["Khan"]))
print("-------------------------")


winner = max(Candidate_Dict, key=Candidate_Dict.get)
print("Winner : " + winner)


#{'Khan': 2218231, 'Correy': 704200, 'Li': 492940, "O'Tooley": 105630}


#Total Votes: 3521001

  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)

#Winner: Khan
print("-------------------------")



    
        