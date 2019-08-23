

def getthesutff(csv):
    months = 0
    total = 0
    maxrev = 0
    minrev = 0
    minrev = 0
    avgchange = 0
    maxmonth = ""
    minmonth = ''
    for row in csv:
        month = row[0]
        pnl = row[1]
        total += 1
        months += pnlmonths += 1
        if pnl > maxrev:
            maxrev = pnl
            maxmonth = current_month
print(months)

return [months, total, maxrev, minrev, avgchange]

with open stuff:
    header = next(csvreader)
    analysis = getthestuff(csvreader)
print(analysis)
