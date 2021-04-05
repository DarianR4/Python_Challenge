#import initial operating stuff
import os
import csv
#set path for pulling CSV file
csvpath = os.path.join("..","Python_Challenge","PyBank","Resources","budget_data.csv")

#with the open file, start running the data
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    
#with open(csvpath) review rows to get counts and print:
    rowcount = -1
    profitcolumn = []
    for row in (csvreader):
        rowcount+= 1  
        profit_loss = int(row[1])
        profitcolumn.append(profit_loss)
    print("Total Months:", rowcount)
    
#run through data The net total amount of "Profit/Losses" over the entire period
    print(f"Net Total Profit/Losses:", (sum(profitcolumn)))
    
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    print("Average Profit and Loss: ")

#The greatest increase in profits (date and amount) over the entire period
    print("Greatest Increase: ")
#The greatest decrease in losses (date and amount) over the entire period
    print("Greatest Decrease: ")