import os
import csv

election_data = os.path.join('.', 'Resources', 'election_data.csv')

with open(election_data, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    header = next(csv_reader)

    total_votes = 0
    khan = 0
    correy = 0
    li = 0
    otooley = 0

    for row in csv_reader:
        total_votes += 1
        if row[2] == "Khan":
            khan += 1
        elif row [2] == "Correy":
            correy += 1
        elif row[2] == "Li":
            li += 1
        elif row[2] == "O'Tooley":
            otooley += 1
    
    print(f"Election Results: {total_votes}")
    print(khan)
    print(correy)
    print(li)
    print(otooley)


    # output = f"Election Results\n" \
    #          f"-------------------------------\n" \
    #          f"Total Votes: {total_votes}\n" \
    #          f"-------------------------------\n"

    # print(output)