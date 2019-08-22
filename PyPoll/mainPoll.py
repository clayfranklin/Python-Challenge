import csv
import os

csvpath = os.path.join("..", "PyPoll", "election_data.csv")

# Open and read csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#The total number of votes cast

    #next(csvreader)
    #row_count = sum(1 for row in csvreader) 
    #print ("Total Votes: " + str(row_count - 1)) 

#curious if there is any repeat voter ID's
    #dup_check =[]
    #next(csvreader)
    #for row in csvreader:
        #dup_check.append(int(row[0]))
        #a = dup_check
        #for i in a:
            #if i in a == i:  
                #print("There are duplicate voter ID's")
            #lse:
                #print( "No duplicate voter ID's!  Election is legit!")

           
#A complete list of candidates who received votes
    #turn list into dictionary
candidates_list = []

file_to_load = os.path.join("..", "PyPoll", "election_data.csv")
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)
    for row in reader:
        candidates_list = len((row[2]))
print(candidates_list)
#The percentage of votes each candidate won
percentage_of_votes = []
#The total number of votes each candidate won
total_votes = []
#The winner of the election based on popular vote. 
winner = []

