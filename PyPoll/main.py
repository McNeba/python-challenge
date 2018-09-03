# Dependencies
import os
import csv
from collections import OrderedDict
from operator import itemgetter

#File to load
csv_path = "../Data/election_data.csv"

#Variables to monitor
votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = {}

# Read CSV File
with open(csv_path, newline="") as csv_file:
    csvreader = csv.DictReader(csv_file, delimiter=',')
    
    for row in csvreader:
        votes = votes + 1
        total_candidates = row["Candidate"]        

        if row["Candidate"] not in candidate_options:
            
            candidate_options.append(row["Candidate"])

            candidate_votes[row["Candidate"]] = 1
            
        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # To determine the Winner:
    #if (votes > winner_votes[2]):
     #   greatest_increase[1] = revenue_change
      #  greatest_increase[0] = row["Candidate"]
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
    print()
    print()
    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(votes))
    print("-------------------------")
#results
    for candidate in candidate_votes:
        print(candidate + ": " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    
candidate_votes

winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

#results
print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")