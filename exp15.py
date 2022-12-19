list1=[12,23,-9,43,32,4]
list2=[31,45,-7,8,18,4]
x=len(list1)
y=len(list2)
s1=sum(list1)
s2=sum(list2)
if(x==y):
    print("List are of same length")
else:
    print("List are of Different length")
if(s1==s2):
    print("Sum of two lists are same")
else:
    print("sum is different")
    print("common elements")
for i in list1:
    for j in list2:
        if(i==j):
            print(i)