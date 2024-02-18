import csv
import os

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #set counter variable to start counting months
    rowcount = 0
    #set total_amount to 0 to start adding to variable at each row, index 1 (P&L data)
    total = 0
    #Returns header and goes to next line in csvreader
    csv_header = next(csvreader)
    #set empty list to deal with first row logic when calculating monthly change
    prev_row = []
    #set monthly_change variable to start cumulating monthly P&L change
    cum_monthly_change = 0
    #set variables to store greatest increase and decrease of profits on each iteration
    greatest_increase = 0
    greatest_decrease = 0
    for row in csvreader:
        date = row[0]
        p_n_l = int(row[1])
        #count of months in data where each row represents a month
        rowcount += 1
        #add the p_n_l value (index 2) at each row iteration to the variable total and replace total
        total += p_n_l
        #if the length of previous row is not 0 (i.e., not the first row)
        if len(prev_row) != 0:
            #creating monthly change variable
            monthly_change = p_n_l - int(prev_row[1])
            #accumulating the monthly_change. taking difference of current month P&L and previous row P&L, adding it to monthly_change 
            cum_monthly_change += p_n_l - int(prev_row[1])
            #compare the monthly change to the greatest_increase; if higher, replace greatest_increase and store the date, row index [0]
            if monthly_change > greatest_increase:
                greatest_increase = monthly_change
                greatest_increase_date = date
            #compare the monthly change to the greatst_decrease; if lower, replace greast_decrease and store the date, row index [0]
            if monthly_change < greatest_decrease:
                greatest_decrease = monthly_change
                greatest_decrease_date = date
        #replacing prev_row variable with current row
        prev_row = row
    #calculate average of changes for the year
    average = format(cum_monthly_change / (rowcount - 1 ), ".2f")
    #print results    
    print(f"Financial Analysis\n ------------------------------\nTotal Months: {rowcount}\nTotal: ${total}\nAverage Change: ${average}\nGreatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\nGreatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
    #export results to text file
    #define path for new output text file
    results_path = os.path.join("analysis", "pybank_results.txt")
    #open file using "write" and specify pybank_results_txt as variable to hold contents
    with open(results_path, "w") as pybank_results_txt:
        pybank_results_txt.write(f"Financial Analysis\n ------------------------------\nTotal Months: {rowcount}\nTotal: ${total}\nAverage Change: ${average}\nGreatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\nGreatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
    

        
        
    




        