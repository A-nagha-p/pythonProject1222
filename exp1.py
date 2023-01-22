x=int(input("enter a the starting year:"))
y=int(input("enter the ending year:"))
print("The following are the leap year.")
for i in range(x,y):
 if((i%400==0) or ((i%100!=0) and (i%4==0))):
     print(i)