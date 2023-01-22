import csv
with open("dep.csv","r")as f:
    r=csv.reader(f)
    for i in r:
        print(i)