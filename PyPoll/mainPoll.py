import csv
import os

csvpath = os.path.join("..", "PyBank", "election_data.csv")



def Answers(csvreader):
    total_votes = 0
    Kahn = 0
    Otool =  0
    Correy = 0
    Li = 0
    percentage_of_votes = float()
    allCandidates = ""
    winner = ""
    
    for row in csvreader:
        votes = row(int(row[2]))
        if row in total_votes is str(Kahn)
            Kahn_votes = Kahn
        if row in total_votes is str(Otool)
            Otool_votes = Otool
        if row in total_votes is str(Correy)
            Correy_votes = Correy
        if row in total_votes is str(Li)
            Li_votes = Li

        





        
    
    
            

#the total number of votes
#The total number of votes each candidate won
#The percentage of votes each candidate won
#The winner of the election based on popular vote. 
return [Kahn, Otool, Correy, Li,]

# Open and read csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",'")
    header = next(csvreader)
    analysis = Answers(csvreader)


#The total number of votes cast
    #next(csvreader)
    #row_count = sum(1 for row in csvreader) 
    #print ("Total Votes: " + str(row_count - 1)) 







