# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    csv_list = [r for r in csvreader]
    max_change = 0
    min_change = 0
    month_counter = 0
    net_total = 0

    first_price = int(csv_list[0][1])
    for row in csv_list:
        month_counter += 1
        net_total = net_total + int(row[1])
        last_price = int(row[1])
    
    # compare max and min price
    for i in range(0,len(csv_list)-1):
        price_this_row = int(csv_list[i][1])
        date_this_row = csv_list[i][0]
        price_next_row = int(csv_list[i+1][1])
        date_next_row = csv_list[i+1][0]
        price_difference = price_next_row - price_this_row
        if price_difference > max_change:
            max_change = price_difference
            max_date = date_next_row
        elif price_difference < min_change:
            min_change = price_difference
            min_date = date_next_row

    #find average change (last price - first price)/month_counter
    average_change = round((last_price - first_price) / (month_counter-1), 2)
    #print all info
    print(
        "Financial Analysis", "\n",
        "-------------------------------","\n",
        "Total Months: " + str(month_counter),"\n",
        "Total: $" + str(net_total),"\n",
        "Average Change: $" + str(average_change),"\n",
        "Greatest Increase in Profits: " + max_date + " ($"+ str(max_change) + ")","\n",
        "Greatest Decrease in Profits: " + min_date + " ($"+ str(min_change) + ")","\n",
    )
   