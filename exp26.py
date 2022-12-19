n=int(input("Enter first number:"))
m=int(input("Enter the second number:"))
gcd=1
for i in range(1,max(n,m)):
    if n%i==0 and m%i==0:
        gcd=i
print("GCD of two numbers is",gcd)