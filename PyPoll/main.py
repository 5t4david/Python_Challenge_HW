import os
import csv
import pandas as pd

csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    Total_Row = 0
    Total_Profit = []

    for row in csvreader:
        print (row)
        Total_Row += 1
    print("Election Results")
    print("--------------------------")
    print("Total Votes: " + str(Total_Row))
    print("--------------------------")
