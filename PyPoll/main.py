import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')
voterInfo = list()
unique_voter = set()
results = list()

with open(csvpath, newline='') as csvfile:
# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #Read the header row first 
    csv_header = next(csvreader)
    voterInfo = list(zip(*csvreader))[2]
    unique_voter = set(voterInfo)

for line in list(sorted(unique_voter)):
    results.append([line, float((voterInfo.count(line) / int(len(voterInfo))) * 100), int(voterInfo.count(line))])

results.sort(key=lambda x: x[2], reverse=True)



# Open the file using "write" mode. Specify the variable to hold the contents
with open("output.txt", 'w', newline='') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("--------------------------------\n")
    txtfile.write("Total votes: " + str(len(voterInfo)))
    txtfile.write("\n--------------------------------\n")

    for line in results:
        txtfile.write(line[0] + ": " + str("{:.2f}".format(line[1])) + "% " + "(" + str(line[2]) + ")\n")
        
    txtfile.write("--------------------------------\n")
    txtfile.write("Winner: " + results[0][0] + "\n")

#print(int(len(voterInfo)))
#print(sorted(unique_voter))
#print(int(len(voterInfo)))
#unique_voter = set(voterInfo)
#print(unique_voter)