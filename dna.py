from sys import argv
import csv
import cs50
# verify arguments are only input of either databasses,sequences and input only has 2 argumetns.
if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)
# store data of people
people = []
# open/read csv files. argument vector 1
with open(argv[1], 'r') as database:
#declared dnareader/header set to read csv file.
    dnareader = csv.DictReader(database)
    header = dnareader.fieldnames
    for row in dnareader:
        people.append(row)
# open/read the sequence files. argumetn vector 2
with open(argv[2]) as sequence:
#declared seq to open and read text in sequences.
    seq = sequence.read().replace('\n', '')
# store the data of dna to match peopel.
dnatoMatch = []
# filter formula to finding the most repeated sequence
for STRs in header[1:]:
#declared n,count and temp
    n = len(seq)-len(STRs)-len(STRs)
    count = 0
    temp = 0
#declared j,start and end.
    for i in range(n):
        j = i + len(STRs)
#STRs equal to seq of i threw j and temp add 1.
        if STRs == seq[i:j]:
            temp += 1
#filter the range of the seq.
            for k in range(round((len(seq)-i)/len(STRs))):
                start = len(STRs) * k
                end = len(STRs) * (k+1)
#seq start is equal to seq end temp add 1.
                if seq[i+start:j+start] == seq[i+end:j+end]:
                    temp += 1
                else:
                    break
            if temp > count:
                count = temp
            temp = 0
    dnatoMatch.append(str(count))
# filter peopledna and dnatomach.
for i in range(len(people)):
#store peopledna
    peopledna = []
    for key, value in people[i].items():
#adding to results of peopledna with append.
        peopledna.append(value)
#reang of peopledna begins at 1 to end equals dnatomach
    if peopledna[1:] == dnatoMatch:
        print(peopledna[0])
        exit(0)
#no results found print no match.
print("No match")
exit(1)