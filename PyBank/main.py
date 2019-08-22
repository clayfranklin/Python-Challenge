import csv
import os

csvpath = os.path.join("..", "PyBank", "budget_data.csv")
#def PnL_Total(stuff):
    #PnL = int(stuff[1])
    #Date = str(stuff[0])

    #total_months = row_count(Date)
    #totalPnL = sum(PnL)

    #return totalPnL 
       

# Open and read csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
 # The total number of months included in the dataset  
#with open("budget_data.csv") as csvfile:
    #headerline = next()
    #total = 0
    #for row in csv.reader:
    #    total += int(row[1])
    #print (total)    
    
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


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    diff = []
    for row in csvreader:
        diff.append(int(row[1]))
        x = diff
        
    differences = []
    for i in range(1,len(x)):
        difference_results = x[i] - x[i-1]
        differences.append(difference_results)
print(differences)







        

    # Python program to get average of a list 
    #next(csvreader)
    #Aver = []
    #for row in csvreader:
    #    Aver.append(int(row[1]))
    #    y = Aver
#print(f"Total Changes : {round(sum(y) / len(y))}")


# Driver Code 


# Printing average of the list 


  
# The greatest increase in profits (date and amount) over the entire period


# The greatest decrease in losses (date and amount) over the entire period
