# Import the os module and csv
import os
import csv

# Path to correct csv file
csvpath = ("Resources/budget_data.csv")


with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # Print header
    print("Financial Analysis")
    print("------------------------------------------------")

    # Total Months and Net total of "Profits/Losses"
    row_count = []
    ProfitsLosses = []
    for row in csvreader:
        row_count.append(row[0])
        ProfitsLosses.append(float(row[1]))
    length_row_count = len(row_count)
    sum_ProfitsLosses = sum(ProfitsLosses)

    # Print Total Months included in dataset, and net total amount of profit/losses over the entire period
    print(f"Total Months: {length_row_count}")
    print(f"Total: ${sum_ProfitsLosses:.0f}")

    # Average Change, Greatest Increase in Profits, Greatest Decrease in Profits
    change = []
    length_ProfitsLosses = len(ProfitsLosses)
    for r in range(1,length_ProfitsLosses):
        # Average change
        change.append(ProfitsLosses[r] - ProfitsLosses[r-1])
        
        # Maximum profit and date
        maxprofit = max(change)
        whereismaxprofit = change.index(maxprofit)+1
        datemaxprofit = (row_count[whereismaxprofit])
        
        # Maximum loss and date
        maxloss = min(change)
        whereismaxloss = change.index(maxloss)+1
        datemaxloss = (row_count[whereismaxloss])
    
    length_change = len(change)
    averagechange = sum(change)/length_change

    # Print the results from this loop
    print("Average Change: $"+"%.2f" % averagechange)
    print(f"Greatest Increase in Profits: {datemaxprofit} (${maxprofit:.0f})")
    print(f"Greatest Decrease in Profits: {datemaxloss} (${maxloss:.0f})")

    output = open("budget_output.txt", "w+")
    print("Financial Analysis", file=output)
    print("------------------------------------------------", file=output)
    print(f"Total Months: {length_row_count}", file=output)
    print(f"Total: ${sum_ProfitsLosses:.0f}", file=output)
    print("Average Change: $"+"%.2f" % averagechange, file=output)
    print(f"Greatest Increase in Profits: {datemaxprofit} (${maxprofit:.0f})", file=output)
    print(f"Greatest Decrease in Profits: {datemaxloss} (${maxloss:.0f})", file=output)
