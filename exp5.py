x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
z=int(input("Enter the third number:"))
if(x>y)and(x>z):
    big=x
elif(y>x)and(y>z):
    big=y
else:
    big=z
print("Biggest number is:",big)