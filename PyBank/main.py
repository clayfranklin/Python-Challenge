import os
import csv

csvpath = os.path.join("..", "PyBank", "budget_data.csv")

# Open and read csv

date = []
pnl = []



# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
 # The total number of months included in the dataset  
    row_count = sum(1 for row in csvreader) 
    print ("Total Months: " + str(row_count - 1))   
   
# this will print all the months with an index value
    #for i in range(len(date)):
        #print("[" + str(i) + "] " + date[i])

# The net total amount of "Profit/Losses" over the entire
    
   
    for row in csvfile:
        total += float(row[column[1])
        print ("Total: " + str(total))
#for pnl in csvreader
#   sum (pnl)
#  print (pnl)
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period