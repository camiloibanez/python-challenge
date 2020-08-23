import os
import csv

file_path = os.path.join("Resources", "election_data.csv")

with open(file_path, 'r') as csvfile:
    election_data_reader = csv.reader(csvfile, delimiter = ',')

    election_data_header = next(election_data_reader)
    # Adding up all votes
    total_votes = 0
    # Having a list of candidates that received at least one vote
    candidates = []
    # Having a list of votes per candidate
    candidates_votes = []

    for row in election_data_reader:
        # Adding a vote to total votes
        total_votes += 1
        candidate = row[2]

        # If candidate not already in list of candidates, add him and start their vote tally at zero
        if candidate not in candidates:
            candidates.append(candidate)
            candidates_votes.append(0)
        # Finding which candidate was voted for
        voted_for_candidate_index = candidates.index(candidate)
        # Adding one vote to his tally
        candidates_votes[voted_for_candidate_index] += 1
        
most_votes = max(candidates_votes)
most_votes_index = candidates_votes.index(most_votes)

winner = candidates[most_votes_index]

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

    # For each candidate find his percent of the vote and his total votes
    for candidate in candidates:
        candidate_index = candidates.index(candidate)
        total_candidate_votes = candidates_votes[candidate_index]
        candidate_vote_percent = total_candidate_votes / total_votes
        rounded_candidate_vote_percent = round(candidate_vote_percent * 100, 3)

        print(f"{candidate}: {rounded_candidate_vote_percent}% ({total_candidate_votes})")
        textfile.write(f"{candidate}: {rounded_candidate_vote_percent}% ({total_candidate_votes})\n")

    textfile.write("-------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("-------------------------\n")

    textfile.close()

print("-------------------------")

print(f"Winner: {winner}")        
print("-------------------------")