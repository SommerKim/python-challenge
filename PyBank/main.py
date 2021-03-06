import os
import csv

#Location of our source of information
budget_data = os.path.join('.', 'Resources', 'budget_data.csv')

# We're using budget_data.csv as our source of information
with open(budget_data, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    header = next(csv_reader)

    #Establishing variable names for the values we're finding
    total_months = 0
    total_profit = 0.0
    last_value = None
    change_sum = 0
    max_increase = 0
    max_increase_date = ""
    max_decrease = 0
    max_decrease_date = ""
    
    # Looping through each row in the csv file
    for row in csv_reader:
        # For each loop, we'll add one to the count of months
        # since each row = 1 month, then add the values for total profit
        total_months += 1
        total_profit += int(row[1])
        # Starting with row 2 (not incl. header), we'll begin calculating
        # the change by subtracting the previous row's profit from the current one.
        if last_value is not None:
            change = int(row[1]) - last_value
            change_sum += change
            # Add the min and max numbers to their respective variables
            # as we loop by comparing previous min/max to current row value
            if int(max_increase) < int(row[1]):
                max_increase = change
                max_increase_date = row[0]
            if int(max_decrease) > int(row[1]):
                max_decrease = change
                max_decrease_date = row[0]
        # Establish current row as last value for next loop
        last_value = int(row[1])
    
    #Calculate and format average change
    average_change = "{:,.2f}".format(change_sum /(total_months - 1))
    
# Write the financial analysis to the terminal and text file
with open(os.path.join('./Analysis', "budget.txt"), 'w') as budget_txt:
    output = f"Financial Analysis\n" \
             f"------------------\n" \
             f"Total Months: {total_months}\n" \
             f"Total: ${round(total_profit)}\n" \
             f"Average Change: ${average_change}\n" \
             f"Greatest Increase in Profits: {max_increase_date} {max_increase}\n" \
             f"Greatest Decrease in Profits: {max_decrease_date} {max_decrease}\n"

    budget_txt.write(output)
    print(output)