#import initial operating stuff
import os
import csv
#set path for pulling CSV file
csvpath = os.path.join("..","Python_Challenge","PyPoll","Resources","election_data.csv")
text_output = os.path.join("..","Python_Challenge","PyPoll","analysis", "election_analysis.txt")
#set parameters
total_votes = 0
winning_count = 0
candidate_votes = {}
candidate_options = []
winning_candidate = ""
#with the open file, start running the data
with open(csvpath) as election_data:
    csvreader = csv.reader(election_data, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        #add the total vote count
        total_votes += total_votes
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name]+1

with open(text_output, "w") as txt_file:
    election_results = (
    f'\n\nElection Results\n'
    f'---------------------\n'
    f'Total Votes: {total_votes}\n'
    f'----------------------\n')
    print(election_results, end=
    '"')

txt_file.write(election_results)
#determine winner
for candidate in candidate_votes:
    votes = candidate_votes.get(candidate)
    vote_percentage = float(votes)/float(total_votes)*100
    if (votes > winning_count):
        winning_count = votes
        winning_candidate = candidate

    voter_output = f'{candidate}: {vote_percentage:.3f}% ({votes})\n'
    print(voter_output, end="")
    text_file.write(voter_output)
    winning_candidate_summary = (
        f'----------------------\n'
        f'Winner: {winning_candidate}\n'
        f'----------------------\n')
    print(winning_candidate_summary)
    text_file.write(winning_candidate_summary)