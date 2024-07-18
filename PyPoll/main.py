print("Election Results")
print("-----------------")

import os
import csv
import pandas as pd

election_csv=os.path.join('PyPoll','Resources','election_data.csv')
df=pd.read_csv(election_csv)

total_votes = 0
candidate_votes = {}
winner = []

with open(election_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    for row in csvreader:
        total_votes += 1

        candidate_name = row[2]
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

print(f"Total Votes: {total_votes}")

winner = []
winner_votes = 0

for candidate_name, votes in candidate_votes.items():
    percentage = round((votes / total_votes) * 100, 3)
    print(f"{candidate_name}: {percentage}% ({votes})")

    if votes > winner_votes:
        winner = candidate_name
        winner_votes = votes

print("-----------------")
print(f"Winner: {winner}")

