#import initial operating stuff
import os
import csv
#set path for pulling CSV file
csvpath = os.path.join('..',"Python_Challenge","PyBank","Resources","budget_data.csv")
#read and confirm path set
with open(csvpath) as csv_file:
    pybank_read = csv.reader(csv_file, delimiter =",")
    print(pybank_read)

#run through dates to print the total dates recorded
    For x in range(10)
    print (x)

#run through data The net total amount of "Profit/Losses" over the entire period


#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period