import csv
import os

# File paths
input_file = os.path.join("Resources", "election_data.csv")
output_result_file = os.path.join("Analysis", "election_results.txt")
output_winner_file = os.path.join("Analysis", "winning_candidate_summary.txt")

# Initialize variables
total_votes = 0
candidates = {}  # Candidate name to vote count dictionary
winner = ""
max_votes = 0

# Read the input file
with open(input_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row

    # Count votes and build candidate dictionary
    for row in reader:
        total_votes += 1
        candidate = row[2]

        if candidate not in candidates:
            candidates[candidate] = 0
        candidates[candidate] += 1

# Calculate results and find the winner
with open(output_result_file, 'w') as result_file:
    result_file.write("Election Results\n")
    result_file.write("-------------------------\n")
    result_file.write(f"Total Votes: {total_votes}\n")
    result_file.write("-------------------------\n")

    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        result_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        if votes > max_votes:
            max_votes = votes
            winner = candidate

    result_file.write("-------------------------\n")
    result_file.write(f"Winner: {winner}\n")
    result_file.write("-------------------------\n")

# Print results to the terminal
with open(output_result_file, 'r') as result_file:
    print(result_file.read())

# Print winning candidate summary to the terminal and a file
with open(output_winner_file, 'w') as winner_file:
    winner_file.write(f"Winner: {winner}\n")

# Print the winning candidate summary to the terminal
with open(output_winner_file, 'r') as winner_file:
    print(winner_file.read())
