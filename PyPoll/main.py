import os
import csv

#Location of our source of information
election_data = os.path.join('.', 'Resources', 'election_data.csv')

# We're using election_data.csv as our source of information
with open(election_data, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    header = next(csv_reader)

    #Establishing variable names for the values we're finding
    total_votes = 0
    khan = 0
    correy = 0
    li = 0
    otooley = 0
    khan_percent = 0.0
    correy_percent = 0.0
    li_percent = 0.0
    otooley_percent = 0.0
    candidates_dict = {}
    winner = ""

    # Looping through each row in the csv file
    for row in csv_reader:
        # Add the votes per candidate
        total_votes += 1
        if row[2] == "Khan":
            khan += 1
        elif row [2] == "Correy":
            correy += 1
        elif row[2] == "Li":
            li += 1
        elif row[2] == "O'Tooley":
            otooley += 1

    # Calcuate and format the percentage of total votes each
    # candidate received        
    khan_percent = "{:,.3%}".format(khan / total_votes)
    correy_percent = "{:,.3%}".format(correy / total_votes)
    li_percent = "{:,.3%}".format(li / total_votes)
    otooley_percent = "{:,.3%}".format(otooley / total_votes)
    # Put candidates into dictionary so we can find the max value
    # and determine the winner
    candidates_dict = {
        "Khan": khan,
        "Correy": correy,
        "Li": li,
        "O'Tooley": otooley
    }
    winner = max(candidates_dict, key=candidates_dict.get)

# Write the election results to the terminal and text file
with open(os.path.join('./Analysis', "election.txt"), 'w') as election_txt:
    output = f"Election Results\n" \
             f"---------------------------------\n" \
             f"Total Votes: {total_votes}\n" \
             f"---------------------------------\n" \
             f"Khan: {khan_percent} ({khan})\n" \
             f"Correy: {correy_percent} ({correy})\n" \
             f"Li: {li_percent} ({li})\n" \
             f"O'Tooley: {otooley_percent} ({otooley})\n" \
             f"---------------------------------\n" \
             f"Winner: {winner}"     

    election_txt.write(output)
    print(output)