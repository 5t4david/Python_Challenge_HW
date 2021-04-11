import os
import csv
import pandas as pd

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    Total_Row = 0
    Total_Profit = []

    for row in csvreader:
        #print (row)
        Total_Row += 1
    print ("Total months: " + str(Total_Row))

with open(csvpath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Total_Profit.append(row["Profit/Losses"])
        Total_Profit_Loss = map(int, Total_Profit)
    #print(Total_Profit)

Sum = sum(Total_Profit_Loss)
print("Total: $"+str(Sum))

