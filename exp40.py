f=open("demo.txt","r")
f1=open("odd.txt","w")
content=f.readlines()
for i in range(0,len(content)):
    if(i%2!=0):
        f1.write(content[i])
    else:
        pass
f.close()
f1.close()
f=open("odd.txt","r")
c=f.read()
print("Odd lines are:",c)
f.close()