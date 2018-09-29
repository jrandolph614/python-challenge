'''create python script that analyzes the following 
The total number of months included in the dataset
The total net amount of "Profit/Losses" over the entire period
The average change in "Profit/Losses" between months over the entire period
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in losses (date and amount) over the entire period'''

import os 
import csv 

csvpath = os.path.join('budget_data.csv')

Date = []
Profit_Loss = []

New_Date = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')

    csvheader = next(csvfile)

    for row in csvreader:
            Date.append(row[0])
            New_Date.append(len(row[0]))
            Profit_Loss.append(int(row[1]))
            
print(sum(Profit_Loss))
   