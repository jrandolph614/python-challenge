
import os 
import csv 
import numpy
import pandas as pd

csvpath = os.path.join('budget_data.csv')

Date = []
Profit_Loss = []
Total_Months = []
New_Date = []
Total_Profit = []
Average = []
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')

    csvheader = next(csvfile)

    for row in csvreader:
            Date.append(row[0])
            New_Date.append(len(row[0]))
            Profit_Loss.append(int(row[1]))
            
Total_Profit = sum(Profit_Loss) 
Total_Months = len(Date)
Average = numpy.mean(Profit_Loss)
dataframe = pd.read_csv('budget_data.csv')

dataframe.head()

def currency(x):
    return '${:,.2f}'.format(x)
dataframe["Profit/Losses"] = dataframe["Profit/Losses"].apply(currency)

dataframe.head()

Total_Profit = '${:,.2f}'.format(Total_Profit)



Average = '${:,.2f}'.format(Average)


data_max = dataframe.loc[dataframe[("Profit/Losses")] == '$999,942.00' , ["Date", "Profit/Losses"] ]


data_min = dataframe.loc[dataframe["Profit/Losses"]== '$-1,022,534.00', ["Date", "Profit/Losses"] ]

Financial_Analysis = pd.DataFrame({"Total Months": [Total_Months], 
                                  "Total Profit": [Total_Profit], 
                                   "Average Change": [Average],
                                   "Greatest Increase in Profits": [data_max],
                                   "Greatest Decrease in Profits": [data_min]})


print("Financial Analysis")
print("--------------------------------")
print("Total Months: ", Total_Months)
print("Total: ", Total_Profit)
print("Average Change: ", Average)
print("Greatest Increase in Profits: ",
      data_max)
print("Greatest Decrease in Profits: ", 
      data_min)

file = open('Financial_Analysis.txt','w')
file.write('Financial Analysis \n')
file.write('-------------------------------- \n')
file.write('Total Months: 86 \n')
file.write('Total:  $38,382,578.00 \n')
file.write('Average Change: $446,309.05 \n')
file.write('Greatest Increase in Profits: \n')
file.write('Date Profit/Losses \n')
file.write('Aug-2013   $999,942.00 \n')
file.write('Greatest Decrease in Profits: \n')
file.write('Date Profit/Losses \n')
file.write('Aug-2012  $-1,022,534.00 \n')
file.close()
    

