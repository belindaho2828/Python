import csv
import os

#use os to join path and store in variable csv_path
csv_path = os.path.join("Resources", "election_data.csv")
with open(csv_path, "r") as election_data:
    #create csv reader to read file
    csvreader = csv.reader(election_data, delimiter = ",")
    #read header and go to next line
    election_header = next(csvreader)
    #define rowcounter to start counting total number of votes cast
    rowcounter = 0
    #create empty dictionary
    vote_count = {}
    for row in csvreader:
        #storing data in variable as defined by row index
        ballot_id = row[0]
        county = row[1]
        candidate = row[2]
        #counting how rows are in data, representative of how many votes cast
        rowcounter +=1
        #if candiate (from index 2 in csvreader) exists in vote_count dictionary, add 1 to its value and replace the value with new total. If candidate does not exist in dictionary, assign it the value of 1
        if candidate in vote_count:
            vote_count[candidate] += 1
        else:
            vote_count[candidate] = 1
    #create empty dictionary to track percentage
    candidate_percent = {}
    #set new variable, winner_votes, as 0 first to compare who has more votes
    winner_votes = 0
    #create lists to hold each element 
    final_results_name = []
    final_results_vote = []
    final_results_percent = []
    #for loop through new candidate_percent dictionary for key name (i.e., candidate) and value (num_votes) from the resulting vote_count dictionary in previous loop
    for name, num_votes in vote_count.items():
        #calculate % based on vote count and total number of votes
        percentage = ((num_votes / rowcounter)*100)
        #assign percentage to each name in dictionary to get per candidate percentage
        candidate_percent[name] = percentage
        #create new list with all the elements needed to print
        final_results_name.append(name)
        final_results_vote.append(num_votes)
        final_results_percent.append(percentage)
        #compare number of votes per candidate in list first to 0 and then to the previous iterated value in dictionary to get max vote and associated candidate name
        if num_votes > winner_votes:
            winner_votes = num_votes
            winner = name
#create empty string to store output:
output = ""
#Append strings to output that need to be printed out:
output += "Election Results\n"
output += "-------------------------\n"
output += f"Total Votes: {rowcounter}\n"
#iterate through each results list, return the results at each corresponding index, and append to output string 
for each_name in range(len(final_results_name)):
    output += f"{final_results_name[each_name]}: {final_results_percent[each_name]:.3f}% ({final_results_vote[each_name]})\n"
output += "-------------------------\n"
output += f"Winner: {winner}\n"
output += "-------------------------\n"

print(output)

#use os to join path for new txt file of results
output_path = os.path.join("analysis", "pypoll_results.txt")
#open file using "write" and specify pypoll_results_txt as variable to hold contents
with open (output_path, "w") as pypoll_results_txt:
        pypoll_results_txt.write(output)



