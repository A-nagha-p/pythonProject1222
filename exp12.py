n=input("Enter string")
a=n[0]
for i in n:
    if i==a:
        n=n.replace(i,'$')
        n=a+n[1:]
print(n)