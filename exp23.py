dict={}
s=input("Enter the string")
for i in s:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
for m,n in dict.items():
   print(m,n)