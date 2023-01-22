import csv
c_col=['ID','Name','Age']
dict_data=[{'ID':1,'Name':'Raoof','Age':100},
           {'ID':2,'Name':'abina','Age':14},
           {'ID':3,'Name':'anu','Age':16},
           {'ID':4,'Name':'sanu','Age':11},
           {'ID':5,'Name':'Manu','Age':50},
           {'ID':6,'Name':'veena','Age':18},
           {'ID':7,'Name':'anjali','Age':20},
           {'ID':8,'Name':'sree','Age':25},
           {'ID':9,'Name':'meenu','Age':23},
           {'ID':10,'Name':'Anju','Age':19},]
try:
    with open("name.csv","w")as f:
        write=csv.DictWriter(f,fieldnames=c_col)
        write.writeheader()
        for i in dict_data:
            write.writerow(i)
except IOError:
    print("Input/output Error")
d=csv.DictReader(open("name.csv"))
print("CSV file output is:")
for i in d:
    print(i)