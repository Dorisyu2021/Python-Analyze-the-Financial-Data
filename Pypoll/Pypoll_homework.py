#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import os
import csv
poll_file=os.path.join("Resources","Resources","election_data.csv")
output_file=os.path.join("Pypoll_homework.txt")

# set the total number as 0
Total_number=0
# define candidate as empty list
Candidates=[]
# define candidate votes  as empty dictionary to get the key pairs
Canvotes={}
# define the winner votes start as 0, winner as empty string
Winnervote=0
Winner=""

with open(poll_file) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    # the first row as header, start the second row
    header=next(csvreader)

    #loop through the dataset, sum the count
    for row in csvreader:
        # add number to last one, loop through the dataset
        Total_number+=1
        
        # find out the candidate name in the list or not. use if function, no name, add it to the candidate list and update the vote number too
        if row[2] not in Candidates:
            Candidates.append(row[2])
            Canvotes[row[2]]=1
        else:
            #if the name in the list, update the vote number only
            Canvotes[row[2]]+=1

#set vR as empty string
vR=""
for Candidates in Canvotes:
    #use get function to get total vots for each candidate
    votesforeach=Canvotes.get(Candidates)
    votesP=f"{(votesforeach/Total_number)*100:,.2f}"
    #use vR to store each candidate match with their votes.+= is important, or only the last candidate show if just use =
    vR+=f"{Candidates}:{votesP}%\n"
    
    # use if function, loop through the candidate vote list, if bigger than compared value,then update the compared value which is the winner vote with new bigger value
    if votesforeach>Winnervote:
        Winnervote=votesforeach
        # match the winner with bigger value
        Winner=Candidates
winneroutput=f"Winner:{Winner}\n"


output=(f"The total number of votes cast is {Total_number}\n"
        f"The Candidates who received votes are {Canvotes}\n"
        f"{vR}\n"
        f"{winneroutput}"
        )
        

print(output)


with open(output_file,"w") as textfile:
    textfile.write(output)

    


