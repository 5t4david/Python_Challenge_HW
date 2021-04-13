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
        #print (row)
        Total_Row += 1
    print("Election Results")
    print("--------------------------")
    print("Total Votes: " + str(Total_Row))
    print("--------------------------")
with open(csvpath) as csvfile:
    csvreader2 = csv.reader(csvfile, delimiter=',')
    for row in csvreader2:
        Polls = pd.DataFrame(csvreader2, columns= ['Voter ID','County','Candidate'])
        Candidates_Count = Polls["Candidate"].value_counts()

        Candidates_Count_df = pd.DataFrame(Candidates_Count)
        Candidates_Count_df = Candidates_Count_df.rename(columns={"Candidate":"Votes"})
        Candidates_Count_df['Percentage']=(Candidates_Count_df['Votes'] /Total_Row)*100

        Candidates_Count_df2 = Candidates_Count_df.sort_values('Percentage', ascending=False)

        High_Vote = (Candidates_Count_df["Percentage"].max())
        High_Ind = str(Candidates_Count_df[Candidates_Count_df['Percentage']==High_Vote].index[0])  

        First_Candidate = Candidates_Count_df.iloc[3:].index[0]
        First_Percentage =(Candidates_Count_df.loc[First_Candidate]['Percentage'])
        First_Votes =(Candidates_Count_df.loc[First_Candidate]['Votes'])
        print(First_Candidate +": " + str(int(First_Percentage))+ "%" + " ("+ str(First_Votes)+")")

        Second_Candidate = Candidates_Count_df.iloc[1:].index[0]
        Second_Percentage =(Candidates_Count_df.loc[Second_Candidate]['Percentage'])
        Second_Votes =(Candidates_Count_df.loc[Second_Candidate]['Votes'])
        print(Second_Candidate +": " + str(int(Second_Percentage))+ "%" + " ("+ str(Second_Votes)+")")

        Third_Candidate = Candidates_Count_df.iloc[2:].index[0]
        Third_Percentage =(Candidates_Count_df.loc[Third_Candidate]['Percentage'])
        Third_Votes =(Candidates_Count_df.loc[Third_Candidate]['Votes'])
        print(Third_Candidate +": " + str(int(Third_Percentage))+ "%" + " ("+ str(Third_Votes)+")")

        Fourth_Candidate = Candidates_Count_df.iloc[3:].index[0]
        Fourth_Percentage =(Candidates_Count_df.loc[Fourth_Candidate]['Percentage'])
        Fourth_Votes =(Candidates_Count_df.loc[Fourth_Candidate]['Votes'])
        print(Fourth_Candidate +": " + str(int(Fourth_Percentage))+ "%" + " ("+ str(Fourth_Votes)+")")
        print("--------------------------")
        print("Winner:  "+ High_Ind)



