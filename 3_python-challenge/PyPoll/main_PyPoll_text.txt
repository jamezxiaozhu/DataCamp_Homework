# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
#running check 1
print(
    "Program running..",
    "\n",
    "\n",
    )
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    csv_list = [r for r in csvreader]
    # The total number of votes cast
    total_votes = 0
    candidate_list_unique = []
    candidate_0_votes = 0
    candidate_1_votes = 0
    candidate_2_votes = 0
    candidate_3_votes = 0
    for row in csv_list:
        total_votes += 1
        # A complete list of candidates who received votes
        if row[2] not in candidate_list_unique:
            candidate_list_unique.append(row[2])
    #running check 2
    print(
        "Almost there!",
        "\n",
        "\n",
        )
    # The total number of votes each candidate won
    for i in range(0,len(csv_list)):
        if csv_list[i][2] == candidate_list_unique[0]:
            candidate_0_votes +=1
        elif csv_list[i][2] == candidate_list_unique[1]:
            candidate_1_votes +=1
        elif csv_list[i][2] == candidate_list_unique[2]:
            candidate_2_votes +=1
        elif csv_list[i][2] == candidate_list_unique[3]:
            candidate_3_votes +=1

    # The percentage of votes each candidate won
    candidate_0_votes_percent = float(candidate_0_votes / total_votes)
    candidate_1_votes_percent = float(candidate_1_votes / total_votes)
    candidate_2_votes_percent = float(candidate_2_votes / total_votes)
    candidate_3_votes_percent = float(candidate_3_votes / total_votes)
    # The winner of the election based on popular vote.
    winner_percent = candidate_0_votes_percent
    winner_name = candidate_list_unique[0]
    if candidate_1_votes_percent > winner_percent:
        winner_percent = candidate_1_votes_percent
        winner_name = candidate_list_unique[1]
    elif candidate_2_votes_percent > winner_percent:
        winner_percent = candidate_2_votes_percent
        winner_name = candidate_list_unique[2]
    elif candidate_3_votes_percent > winner_percent:
        winner_percent = candidate_3_votes_percent
        winner_name = candidate_list_unique[3]

 
    #print all info

    print(
        "Election Results", "\n",
        "-------------------------","\n",
        "Total Votes: " + str(total_votes),"\n",
        "-------------------------","\n",
        str(candidate_list_unique[0])+ ": "+ "{:.3%}".format(candidate_0_votes_percent) + " ("+ str(candidate_0_votes) +")","\n",
        str(candidate_list_unique[1])+ ": "+ "{:.3%}".format(candidate_1_votes_percent) + " ("+ str(candidate_1_votes) +")","\n",
        str(candidate_list_unique[2])+ ": "+ "{:.3%}".format(candidate_2_votes_percent) + " ("+ str(candidate_2_votes) +")","\n",
        str(candidate_list_unique[3])+ ": "+ "{:.3%}".format(candidate_3_votes_percent) + " ("+ str(candidate_3_votes) +")","\n",
        "-------------------------","\n",
        "Winner: " + winner_name
    ) 
    with open("output.txt", "a") as f:
        print(
            "Election Results", "\n",
            "-------------------------","\n",
            "Total Votes: " + str(total_votes),"\n",
            "-------------------------","\n",
            str(candidate_list_unique[0])+ ": "+ "{:.3%}".format(candidate_0_votes_percent) + " ("+ str(candidate_0_votes) +")","\n",
            str(candidate_list_unique[1])+ ": "+ "{:.3%}".format(candidate_1_votes_percent) + " ("+ str(candidate_1_votes) +")","\n",
            str(candidate_list_unique[2])+ ": "+ "{:.3%}".format(candidate_2_votes_percent) + " ("+ str(candidate_2_votes) +")","\n",
            str(candidate_list_unique[3])+ ": "+ "{:.3%}".format(candidate_3_votes_percent) + " ("+ str(candidate_3_votes) +")","\n",
            "-------------------------","\n",
            "Winner: " + winner_name,
            file = f
        )         
# Sample Results:
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------
# 