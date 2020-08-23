import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

Total_votes = 0
Candidates = 0
Khan = 0
Otooley = 0
Correy = 0
Li = 0

Candidates = ["Khan", "Otooley", "Correy", "Li"]
Total_votes = [khan, otooley, correy, Li]

candidates_and_Total_votes = dict[zip(Candidates, Total_votes)]
key = max(Candidates_and_Total_votes.get)
key = max(Candidates_and_Total_votes.get)

with open(csv_file_path, newline="") as election_data:

    csvreader = csv.reader(election_data, delimiter=',') 

    header = next(csvreader) 

for row in csvreader:

      if row[2] == ("Khan"): 
            khan +=1
        elif row[2] == ("Otooley"):
            Otooley +=1
        elif row[2] == ("Correy"): 
            Correy +=1
        elif row[2] == ("Li"):
            Li +=1

        Total_votes +=1


Vote_percentage_Khan = (Khan/Total_votes)*100
Vote_percentage_Otooley = (Otooley/Total_votes)*100 
Vote_percentage_Correy = (Correy/Total_votes)*100
Vote_percentage_Li = (Li/Total_votes)*100


print("Election Results")
print("----------------------------")
print("Total Votes: " + str(Total_votes))
print("----------------------------")
print(f"Khan: {Vote_percentage_Khan:.3f} +str(%) {Khan}")
print(f"Correy: {Vote_percentage_Otooley:.3f} +str(%) {Otooley}")
print(f"Li: {Vote_percentage_Correy:.3f} +str(%) {Correy}")
print(f"O'Tooley: {Vote_percentage_Li:.3f} +str(%) {Li}")
print("Winner: " + str(key))
print("----------------------------")


ElectionResult.write("Election Results")
ElectionResult.write("\n")
ElectionResult.write("----------------------------")
ElectionResult.write("\n")
ElectionResult.write("Total Votes: " + str(Total_votes))
ElectionResult.write("\n")
ElectionResult.write("----------------------------")
ElectionResult.write("\n")
ElectionResult.write(f"Khan: ({Vote_percentage_Khan:.3f}+str(%)) ({Khan})")
ElectionResult.write("\n")
ElectionResult.write(f"Otooley: ({Vote_percentage_otooley:.3f}+str(%)) ({otooley})")
ElectionResult.write("\n")
ElectionResult.write(f"Correy: ({Vote_percentage_Correy:.3f}+str(%)) ({Correy_votes})")
ElectionResult.write("\n")
ElectionResult.write(f"Li: ({Vote_percentage_Li:.3f}+str(%)) ({Li})")
ElectionResult.write("\n")
ElectionResult.write("----------------------------")
