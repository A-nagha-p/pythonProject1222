class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
            return self.length*self.breadth
    def perimeter(self):
            return (2*(self.length+self.breadth))
l=int(input("Enter the length of first rectangle:"))
b=int(input("Enter the breadth of first rectangle:"))
x=rectangle(l,b)
y=x.area()
z=x.perimeter()
print("The area is:",y)
print("The perimeter is:",z)
l1=int(input("Enter the length of second rectangle:"))
b1=int(input("Enter the breadth of second rectangle:"))
x1=rectangle(l1,b1)
d=x1.area()
f=x1.perimeter()
print("The area is:",d)
print("The perimeter is:",f)
if(y>d):
    print("The first rectangle is greater than second rectangle")
else:
    print("The second rectangle is greater than first rectangle")