import os
import csv

budget_data = os.path.join('.', 'Resources', 'budget_data.csv')

with open(budget_data, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    header = next(csv_reader)

    #find the total in the profit/losses column [1]
    total_months = 0
    total_profit = 0.0
    last_value = None
    change_sum = 0
    max_increase = 0
    max_increase_date = ""
    max_decrease = 0
    max_decrease_date = ""
    
    for row in csv_reader:
        total_months += 1
        total_profit += int(row[1])
        if last_value is not None:
            change = int(row[1]) - last_value
            change_sum += change
            if int(max_increase) < int(row[1]):
                max_increase = change
                max_increase_date = row[0]
            if int(max_decrease) > int(row[1]):
                max_decrease = change
                max_decrease_date = row[0]
        last_value = int(row[1])

    average_change = change_sum /(total_months - 1)
    average_change = "{:,.2f}".format(average_change)
    

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