#import initial operating stuff
import os
import csv
#set path for pulling CSV file
csvpath = os.path.join("..","Python_Challenge","PyBank","Resources","budget_data.csv")
text_output = os.path.join("..","Python_Challenge","PyBank","analysis", "budget_analysis.txt")
#with the open file, start running the data
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    
#set parameters for financials
    rowcount = 0
    profitcolumn = []
    month_of_change = []
    net_change_list = []
    greatest_increase = ["",0]
    greatest_decrease = ["",9999999999999999]
    total_net = 0

    first_row = next(csvreader)
    total_months = 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])
    for row in csvreader:
        total_months += 1
        total_net += int(row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]
    if net_change > greatest_increase[1]:
        greatest_increase[0] = row[0]
        greatest_increase[1] = net_change
    if net_change < greatest_decrease[1]:
        greatest_decrease[0] = row[0]
        greatest_decrease[1] = net_change  
    
#run through data The net total amount of "Profit/Losses" over the entire period
    print("Total Months:", total_months)
    print(f"Net Total Profit/Losses:", total_net)
    
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    net_monthly_avg = sum(net_change_list) / len(net_change_list)
    print("Average Profit and Loss: ", net_monthly_avg)

#The greatest increase in profits (date and amount) over the entire period
# Track the net change
    net_change = int(row[1]) - prev_net
    prev_net = int(row[1])
    net_change_list += [net_change]
    month_of_change += [row[0]]
    # Calculate the greatest increase
   
    print("Greatest Increase: ", greatest_increase[0], greatest_increase[1])
#The greatest decrease in losses (date and amount) over the entire period
     
    print("Greatest Decrease: ", greatest_decrease[0], greatest_decrease[1])

with open(text_output, "w") as txt_file:
   txt_file.write(text_output)
