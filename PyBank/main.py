import os
import csv

budget_data = os.path.join('.', 'Resources', 'budget_data.csv')

print(budget_data)

with open(budget_data, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    header = next(csv_reader)

    #find the total in the profit/losses column [1]
    total_months = 0
    total_profit = 0.0
    last_value = None
    change_sum = 0

    for row in csv_reader:
        total_months += 1
        total_profit += int(row[1])
        if last_value is not None:
            change = int(row[1]) - last_value
            change_sum += change
        last_value = int(row[1])
        
    average_change = change_sum /(total_months - 1)
    average_change = "{:,.2f}".format(average_change)
    
    
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${average_change})