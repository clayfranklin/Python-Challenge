import os
import csv

csvpath = os.path.join("..", "PyBank", "budget_data.csv")

# Open and read csv

date = []
pnl = []



# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add title
        date.append(row[0])

        # Add price
        pnl.append(row[1])

    #print (date)
    #print (pnl)

# The total number of months included in the dataset
    for i in range(len(date)):
        print("[" + str(i) + "] " + date[i])

# The net total amount of "Profit/Losses" over the entire period
    #for pnl in csvreader
     #   sum (pnl)
      #  print (pnl)
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period