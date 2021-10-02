#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

import os
import csv

Pybank_file=os.path.join("Resources","budget_data.csv")
Output_file=os.path.join("Pybank_homework.txt")

# define total months and start count at 0
Total_month=0
# define total amount in P/L and atart count at 0
Total_amount=0
# define monthly change to a list with every month change, current minus previous amount
Monthlychange=[]
# months list updated with month change
Months=[]

with open(Pybank_file) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    # defined header, including column names
    header=next(csvreader)
    # this is the row where data start to run
    firstrow=next(csvreader)
    
    # as the first row[1], this is the basic of all calculation as the first past amount. need to defined as float
    pastchange=float(firstrow[1])
    # loop to next month 
    Total_month+=1
    
    
    for row in csvreader:
        # loop to next month then add up
        Total_month+=1
        # loop to next amount then add up
        Total_amount+=float(row[1])
        
        #calculate the differences
        netchange=float(row[1])-pastchange
        # make the results add to month change list
        Monthlychange.append(netchange)
        # update months list with month change
        Months.append(row[0])
        # update the previous amount with next row
        pastchange=float(row[1])

avechange=sum(Monthlychange)/len(Monthlychange)

#the greatest and smallest number is always the first one
greatIn=[Months[0],Monthlychange[0]]
greatDe=[Months[0],Monthlychange[0]]

# let g loop through the len of month change
for g in range(len(Monthlychange)):
    # use if function, compare to the index 1, which is the amount column.if it's> index 1 value, then update great value with g value. loop to next row
    if(Monthlychange[g]>greatIn[1]):
        greatIn[1]=Monthlychange[g]
        greatIn[0]=Months[g]
    # same like great increase. if g< index 1,then update great decrease with g
    if(Monthlychange[g]<greatDe[1]):
        greatDe[1]=Monthlychange[g]
        greatDe[0]=Months[g]


Output=(f"There are {Total_month} months.\n"
        f"The total amount of profit/losses is {Total_amount:,.2f}\n"
        f"The average monthly change is {avechange:,.2f}\n"
        f"The great increast month is {greatIn[0]} and amount is{greatIn[1]:,.2f}\n"
        f"The great decreast month is {greatDe[0]} and amount is {greatDe[1]:,.2f}\n")
    
print(Output)

with open(Output_file,"w") as textfile:
    textfile.write(Output)
        








