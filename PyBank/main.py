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

    for row in csv_reader:
        total_months += 1
        total_profit += int(row[1])
        
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: $ {total_profit}")
