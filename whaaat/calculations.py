import csv

rahad = {"Mati":0,"Anna":0,"Kati":0,"Markus":0}

with open('maksed.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    linenr = 0
    for l in csv_reader:
        if linenr == 0:
            linenr+=1
            pass
        else:
            rahad[l[1]] += int(l[2])
            rahad[l[0]] -= int(l[2])
    
for person in rahad:
    if rahad[person] < 0:
        print(f'{person} volgneb {abs(rahad[person])} eurot')
    elif rahad[person] > 0:
        print(f'{person} teenib {abs(rahad[person])} eurot')

        