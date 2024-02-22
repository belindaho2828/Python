# Python #
For both PyBank and PyPoll, Analysis was performed on data in a csv file by importing the os and csv modules in Python and the associated functions. The results were then printed on the terminal as well as exported into a text file. 
## OS Path ##
path.join was used to join and store the path of the provided csv data file from the resources folder
## Open, Read, Next, and Write functions##
The Open function was used to find the csv file and access it by using the path stored previously. Csv.reader was used to read the csv file and stored in variable "csvreader". Since both csv files for PyBank and PyPoll consisted of headers, Next function was used to read the header and go to the next row. The Write function was then invoked to write the results of the analysis to a text file and store it in the "analysis" folder (path was determined using the OS path function again). 
# PyBank #
The CSV source file consisted of 2 data points at index [0] and [1] for each row (i.e., new line). The date was at index[0] and the associated profit/loss was at index[1]. 

Each new line represented one month of data. A for loop was used to iterate through each row in the CSV file. 
I used "row +=1" and "total += p_n_l" to count the number of rows (excluding headers) and accumulate the sum of each month's profit/loss (after declaring p_n_l = row[1]) and stored them in their respective variables to give a result of 86 months worth of data and $22564198 total profit. 

To calculate the monthly change in profit/loss, each row's information was stored in "prev_row" variable to be referenced back when iterating on the next row. On the next iteration, the difference between current row and previous row is taken at index 1 (profit/loss) and stored in "monthly_change" variable and accumulated in "cum_monthly_change variable".

See "pybank_results" in PyBank analysis folder and individual comments in code stored in "main.py" file for more details.


# PyPoll # 
Analysis was performed on data represented in a csv file to report on election results, where each row (new line) in the source file represented a vote. Ballot id was indexed at [0], county at [1], and candidate at [2]. 

New dictionary "vote_count" created to store the count for each vote with logic: if candidate value exists in dictionary, add 1 vote count; otherwise, add the candidate and assign it a value of 1 (votes will be added to this later as the for loop comes across the name again). Another dictionary, candidate_percent, is created using items from vote_count dictionary to calculate total percentage of votes per candidate. winner_votes variable was used to compare number of votes per candidate to determine the winner, Diana DeGette.

To print the final results, 3 lists were created with 3 elements each (representing each candidate): name, number of votes, and percentages. The lists containing the results and string literals were then added to output variable to print the results and export in a text file.

See "pypoll_results" in PyPoll analysis folder and individual comments in code stored in "main.py" file for more details.

# Acknowledgements #
    For PyPoll, I used ChatGPT to figure out how to create an empty string and append to it in order to print literal string along with results contained in variables (indicated as "output +=" in code). 
    
    I also used outside tutoring for the idea to create a 2nd dictionary in PyPoll and how to build in logic when comparing the first row in PyBank *i.e., if len(prev_row) !=0. 

    For all else, I referred to concepts shown in class (notes and Zoom recording) and used Google search for further understanding of concepts (as well as Python documentation).



    