# Dependencies
import os
import csv

# File to Load
csv_path = "../Data/budget_data.csv"

# Variables to observe 
total_months = 0
total_profit_losses = 0

initial_profit_losses = 0
profit_losses_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

profit_losses_changes = []

# Read CSV File
with open(csv_path, newline="") as csv_file:
    csvreader = csv.DictReader(csv_file, delimiter=',')

    # Loop through all the rows of data we PyBank data
    for row in csvreader:

        # Calculate the totals for each column
        total_months = total_months + 1
        total_profit_losses = total_profit_losses + int(row["Profit/Losses"])
        # print(row) but reseverved for later

        # Keep track of changes
        profit_losses_change = int(row["Profit/Losses"]) - initial_profit_losses
        # print(profit_losses_change)

        # Reset the value of initial_profit_losses to the row I completed my analysis
        Initial_profit = int(row["Profit/Losses"])
        # print(initial_profit_losses)

        # Determine the greatest increase
        if (profit_losses_change > greatest_increase[1]):
            greatest_increase[1] = profit_losses_change
            greatest_increase[0] = row["Date"]

        if (profit_losses_change < greatest_decrease[1]):
            greatest_decrease[1] = profit_losses_change
            greatest_decrease[0] = row["Date"]

        # Add to the profit_losses_changes list
        profit_losses_changes.append(int(row["Profit/Losses"]))

    # Set the profit_losses average
    avg_profit_losses = sum(profit_losses_changes) / len(profit_losses_changes)
    
    # Print Output
    print()
    print()
    print()
    print()
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total Profit_Losses: " + "$" + str(total_profit_losses))
    print("Average Change: " + "$" + str(round(sum(profit_losses_changes) / len(profit_losses_changes),2)))
    print("Greatest Increase in Profits: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease in Profits: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")