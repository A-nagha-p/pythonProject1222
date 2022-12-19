dict={}
s=str(input("Enter the sentance:"))
word=s.split(" ")
for i in word:
    if i in dict:
        dict[i]:dict[i]+1
    else:
        dict[i]=1
for m,n in dict.items():
    print(m,n)