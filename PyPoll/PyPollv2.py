    
#import csv document
import csv
import os
from collections import Counter

csvpath = os.path.join("..", "PyPoll", "election_data.csv")

# set placeholders

Candidates = []
Candidate_Dict = {}
Candidate_votes = {}
total = 0
winner = 0


print("    Election Results")

# Loop through with foreach loop to find total votes cast

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
        
    print("  -------------------------")
    for row in csvreader:
        total += 1
print("Total Votes: " + (str(total)))

# reopen as it has been used

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
# tally individual candidates with counter
# store and convert to dictionary
#         
    print("-------------------------")
    for row in csvreader:
        Candidate_Name = row[2]
        Candidates.append(Candidate_Name)
    Candidate_Dict = dict(Counter(Candidates))

# calculate percentages using key value pairs

Khan_percent = Candidate_Dict["Khan"]*100/total
Khan_percent = round(Khan_percent)

Correy_percent = Candidate_Dict["Correy"]*100/total
Correy_percent = round(Correy_percent)

Li_percent =Candidate_Dict["Li"]*100/total
Li_percent = round(Li_percent)

Otooly_percent = Candidate_Dict["O'Tooley"]*100/total
Otooly_percent = round(Otooly_percent)

#print analysis

print("Khan: " , str(Khan_percent) + "%" , str(Candidate_Dict["Khan"]))
print("Correy: " , str(Correy_percent) + "%" , str(Candidate_Dict["Correy"]))
print("Li: " , str(Li_percent) + "%" , str(Candidate_Dict["Li"]))
print("O'Tooly: " , str(Otooly_percent) + "%" , str(Candidate_Dict["O'Tooley"]))
print("-------------------------")


winner = max(Candidate_Dict, key=Candidate_Dict.get)
print("Winner : " + winner)





#Winner: Khan
print("-------------------------")


#print analysis to txt.  I don't know how to do this
#and I think it's becuase I'm doing too many things to my 
#print statements.  Is it too klunky?

#output(
   # printf"\n    Election Results\n"
    #printf"  -------------------------\n"
    #printf"Total Votes: " + (str(total))
    #printf"-------------------------"
    #printf"Khan: " , str(Khan_percent) + "%" , str(Candidate_Dict["Khan"])
    #printf"Correy: " , str(Correy_percent) + "%" , str(Candidate_Dict["Correy"])
    #printf"Li: " , str(Li_percent) + "%" , str(Candidate_Dict["Li"])
    #printf"O'Tooly: " , str(Otooly_percent) + "%" , str(Candidate_Dict["O'Tooley"])
    #printf"-------------------------"
    #printf"Winner : " + winner)


#export as txt file
#with open(file_to_output, "a") as txt_file:
    #txt_file.write(output)