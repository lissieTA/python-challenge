import os

# Module for reading CSV files
import csv
#import datetime
#from dateutil.parser import parse
from statistics import mean

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# opening csv
listDates = []
months_count = 0
profit_changes = []
difference = []
with open(csvpath, newline='') as csvfile:
# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    for row in csvreader:
        #listDates.append(parse(row[0]))
        listDates.append(row[0])
        profit_changes.append(float(row[1]))

months_count = len(listDates)

i = 0

for i in range(i, months_count - 1):
    difference.append(profit_changes[i+1] - profit_changes[i])
    #print(str(difference[i]))

maxChange = max(difference)
minChange = min(difference)
with open("output.txt", 'w', newline='') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("--------------------------------\n")
    txtfile.write("Total Months: " + str(months_count) + "\n")
    txtfile.write("Total: $" + str(sum(profit_changes)) + "\n")
    txtfile.write("Average Change: $" + str(sum(profit_changes)) + "\n" )
    txtfile.write("Greatest Increase in Profits: " + listDates[difference.index(maxChange) + 1] + " ($" + str(maxChange) + ")\n")
    txtfile.write("Greatest Decrease in Profits: " + listDates[difference.index(minChange) + 1] + " ($" + str(minChange) + ")\n")
#print(months_count)
#print(sum(profit_changes))
#print(mean(profit_changes))


#print(str(max(difference)))
#print(str(min(difference)))

#print("number " + str(profit_changes[i+1]) + " minus " + str(profit_changes[i]) + " equals " + str(profit_changes[i+1] - profit_changes[i]))
#+ profit_changes[i] + "equals" + (profit_changes[i+1] - profit_changes[i)])
    
