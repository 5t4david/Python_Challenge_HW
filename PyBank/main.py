import os
import csv
import pandas as pd

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    Total_Row = 0
    Total_Profit = []

    for row in csvreader:
        #print (row)
         Total_Row += 1
    print ("Total months: " + str(Total_Row))

with open(csvpath) as csvfile:
    csvreader2 = csv.reader(csvfile, delimiter=',')
    for row in csvreader2:
        pbank = pd.DataFrame(csvreader2, columns= ['Date','Profit/Losses'])
        pbank.loc[:, "Profit/Losses"] = pbank["Profit/Losses"].astype("float")

        Sum = sum(pbank["Profit/Losses"])
        print("Total: $"+str(Sum))

        df = pd.DataFrame({ 'Profit/Losses': pbank["Profit/Losses"]})
        df['output']=df['Profit/Losses'] -df['Profit/Losses'].shift(1)
        #print(df)
        
        df2 = pd.merge(pbank, df, on='Profit/Losses', how='outer')

        Avr_Chg = (df["output"].sum())
        print("Average Change: $" + str(Avr_Chg/Total_Row))

        High_Profit = (df["output"].max())
        print("Greatest Increase in Profit: $" + str(High_Profit))

        High_Loss = (df["output"].min())
        print("Greatest Increase in Loss: $" + str(High_Loss))



        
