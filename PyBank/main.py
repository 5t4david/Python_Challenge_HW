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
    Total_Loss = []

    for row in csvreader:
        #print (row)
        Total_Row += 1
    print ("Total months: " + str(Total_Row))
with open(csvpath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Total_Profit.append(row["Profit/Losses"])
    #print(Total_Profit)

    Data = {"Profit/Losses": [Total_Profit]}
    df = pd.DataFrame(Data)
    df["Profit/Losses"] = pd.to_numeric(df["Profit/Losses"])
    print(df)
    print(df.dtypes)