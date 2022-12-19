n=int(input("Enter the number of elements"))
list=[]
print("enter the elements")
for i in range(0,n):
    ele=int(input())
    if(ele>100):
        list.append("over")
    else:
        list.append(ele)
print(list)