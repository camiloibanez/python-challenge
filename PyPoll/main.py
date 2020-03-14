import os
import csv

file_path = os.path.join("Resources", "election_data.csv")

with open(file_path, 'r') as csvfile:
    election_data_reader = csv.reader(csvfile, delimiter = ',')

    election_data_header = next(election_data_reader)

    total_votes = 0
    candidates = []
    candidates_votes = []

    for row in election_data_reader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            candidates_votes.append(0)

        candidates_votes[candidates.index(row[2])] += 1
        
winner = candidates[candidates_votes.index(max(candidates_votes))]

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

output_path = os.path.join("election_results.txt")

with open(output_path, 'w') as textfile:
    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-------------------------\n")

    for candidate in candidates:
        candidate_vote_percent = round((candidates_votes[candidates.index(candidate)] / total_votes) * 100, 3)
        print(f"{candidate}: {candidate_vote_percent}% ({candidates_votes[candidates.index(candidate)]})")
        textfile.write(f"{candidate}: {candidate_vote_percent}% ({candidates_votes[candidates.index(candidate)]})\n")

    textfile.write("-------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("-------------------------\n")

    textfile.close()

print("-------------------------")

print(f"Winner: {winner}")        
print("-------------------------")