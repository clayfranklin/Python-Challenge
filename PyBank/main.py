import csv
import os

csvpath = os.path.join("..", "PyBank", "budget_data.csv")

# Open and read csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
 # The total number of months included in the dataset     
    
    row_count = sum(1 for row in csvreader) 
    print ("Total Months: " + str(row_count - 1))   
   
# The net total amount of "Profit/Losses" over the entire time
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    PnL = []
    for row in csvreader:
        PnL.append(int(row[1]))
        x = PnL
print(f"Total : {(str(sum(x)))}")
    
# The average of the changes in "Profit/Losses" over the entire period

# create new list with all the values minus the header
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    diff = []
    date = []
    for row in csvreader:
        diff.append(int(row[1]))
        x = diff
        
# create a new list with the differences over each increment
    differences = []
    for i in range(1,len(x)):
        difference_results = x[i] - x[i-1]
        differences.append(difference_results)
# bart that shit up into a single number to average
        barf = (str(sum(differences)))
# print that barfy stew's average


  
# The greatest increase in profits (date and amount) over the entire period

# loop through the list and return the highest value
        high = (max(differences))
        low = (min(differences))

print("Average Change: " + str(round(int(barf)/85)))
print(high)
print(low)
           
# find the index of that value
print(differences.index(high))

# print the index of column [0] with the result from column [1], 

# The greatest decrease in losses (date and amount) over the entire period
