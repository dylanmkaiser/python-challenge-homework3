# Import the os module and csv
import os
import csv

# Path to correct csv file
csvpath = ("Resources/election_data.csv")

total_results = 0
candidates = []
candidate_votes = {}
winnervotes = 0
winner = []

# Open a new txt file
output = open("poll_output.txt","w+")

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    csvheader = next(csvreader)
    # Print and write header
    print("Election Results")
    print("-------------------------")
    print("Election Results", file=output)
    print("-------------------------", file=output)
    
    # For loop for total votes and candidate names
    for row in csvreader:
        # Find total votes
        total_results = total_results + 1
        # Find list of candidates and record votes
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]] = 0
        candidate_votes[row[2]] = candidate_votes[row[2]] + 1
    
    # Print and write total votes
    print(f"Total Votes: {total_results}")
    print("-------------------------")
    print(f"Total Votes: {total_results}", file=output)
    print("-------------------------", file=output)
    
    # For loop to find amount of votes for each candidate, and convert that to
    # a percentage of total votes
    for candidates in candidate_votes:

        votecount = candidate_votes.get(candidates)
        votefraction = float(votecount)/float(total_results)
        percent = votefraction * 100
        
        # Print and write each candidate, percentage of votes they won, and count of votes they won
        print(f"{candidates}: {percent:.3f}% ({votecount})")
        print(f"{candidates}: {percent:.3f}% ({votecount})", file = output)
    
    # For loop to find the winner
    for candidates in candidate_votes:
        if (votecount > winnervotes):
            winnervotes = votecount
            winner = candidates
        

    # Print and write winner name
    print("-------------------------")
    print("Winner: "+str(winner))
    print("-------------------------")
    print("-------------------------", file=output)
    print("Winner: "+str(winner), file=output)
    print("-------------------------", file=output)





    