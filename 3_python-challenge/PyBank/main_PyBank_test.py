# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_new = [r for r in csvreader]

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    month_counter = 0
    net_total = 0
    max_change = 0
    min_change = 0
    first_price = csv_new[1][1]

    # Read each row of data after the header
    # increment count after each row, add total to net_total
    for row in csv_new:
        first_price = row[1]
        month_counter += 1
        net_total = net_total + row[1]
        last_price = [row][1]
        price_this_row = [row][1]
        date_this_row = [row][0]
        price_next_row = [row +1][1]
        date_next_row = [row][0]
        price_difference = price_next_row - price_this_row
        if price_difference > max_change:
            max_change = price_difference
            max_date = date_next_row
        elif price_difference < min_change:
            min_change = price_difference
            min_date = date_next_row
#    
#    
#    #find average change (last price - first price)/month_counter
#    average_change = (last_price - first_price) / month_counter
#
#    #print all info
#    print(
#        "Financial Analysis", 
#        "-------------------------------",
#        "Total Months: " + str(month_counter),
#        "Total: " + str(net_total),
#        "Average Change: " + str(average_change),
#        "Greatest Increase in Profits: " + max_date + str(max_change),
#        "Greatest Decrease in Profits: " + min_date + str(min_change)
#
#    )
#
