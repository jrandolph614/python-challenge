
import pandas as pd 
import os 
import numpy

df = pd.read_csv('election_data.csv')

df.head()

Total_Votes = df['Voter ID'].count()


print(df['Voter ID'].count())


df['Candidate'].unique()


print(df['Candidate'].unique())


Total_Votes = df['Candidate'].value_counts()

Total_Votes

Total_Votes_Percent = df['Candidate'].value_counts(3521001)


Total_Votes_Percent = Total_Votes_Percent *100 

Total_Votes_Percent


print("Election Results")
print("-------------------------------")
print("Khan: 63.00% (2218231)") 
print("Correy: 19.99% (704200)")
print("Li:  13.99% (492940)")
print("O'Tooley:  2.99% (105630)")
print("-------------------------------")
print("Winner: Khan")
print("-------------------------------")


file = open('Election_Results.txt','w')
file.write("Election Results \n")
file.write('-------------------------------- \n')
file.write('Khan: 63.00% (2218231) \n')
file.write('Correy: 19.99% (704200) \n')
file.write('Li:  13.99% (492940) \n')
file.write("O'Tooley:  2.99% (105630) \n")
file.write("------------------------------- \n")
file.write('Winner: Khan \n')
file.write('------------------------------- \n') 
file.close()
