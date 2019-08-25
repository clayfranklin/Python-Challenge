import csv
import os

csvpath = os.path.join("..", "PyPoll", "election_data.csv")
 
def Answers(csvreader):
    voted_list = list(row[2])
    Khan_votes = 0
    votes = 0
    for row in csvreader:
        votes = row[2]
        if votes is "Khan":
            Khan_votes += 1
    
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    Khan_votes = Answers(csvreader)
    print(f"{Khan_votes}")


# Open and read csv 

#the total number of votes
#The total number of votes each candidate won
#The percentage of votes each candidate won
#The winner of the election based on popular vote. 
# Open and read csv
#The total number of votes cast
    #next(csvreader)
    #row_count = sum(1 for row in csvreader) 
    #print ("Total Votes: " + str(row_count - 1)) 







