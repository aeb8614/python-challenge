vote_data = "election_data_1.csv"
import csv
voter = []
candidate = []

with open(vote_data, newline='') as csvfile:
    vote_lists = csv.reader(csvfile, delimiter=',')
    for row in vote_lists:
        voter.append(row[0])
        candidate.append(row[2])

#total number of votes
total_votes = len(voter)

#counting votes
from collections import Counter
counts = Counter(candidate)
candidate_results = dict(counts)
del candidate_results["Candidate"]

#converting votes count dictionary to 2 lists
candidate_names = list(candidate_results.keys())
vote_counts = list(candidate_results.values())

#calculating the percent results
percent_results = []
for votes in vote_counts:
    percent = (votes/total_votes)*100
    percent_results.append(round(percent,1))

    #zipping the three lists together and printng the results; b/c the counter sorts the results largest to smallest the winner will always be index 0
results = zip(candidate_names, percent_results, vote_counts)
print("Election Results")
print("-----------------------")
print("Total Votes: " + str(total_votes))
print("-----------------------")
for candidate in results:
    print(candidate[0] + ": " + str(candidate[1]) + "% " + "(" + str(candidate[2]) + ")")
print("-----------------------")
print("Winner: " + candidate_names[0])