import os
import csv

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
    
    #row_count = sum(1 for row in csvreader) 
    #print ("Total Months: " + str(row_count - 1))   
   
# The net total amount of "Profit/Losses" over the entire time
    next(csvreader)
    for row in csvreader:
        PnL = [row[1]]
        x = sum(PnL) 
        print("Total:  " + int(x))

        

    # make placeholder
    #store all the values in a list 
    
    
               

    #for row in csvreader:
        #Date = [row[0]]
        


    #sum all the numbers and print
    


# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period