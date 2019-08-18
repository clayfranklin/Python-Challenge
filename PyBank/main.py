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

    print (date)
    print (pnl)