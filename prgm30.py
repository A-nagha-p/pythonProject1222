lis=[]
x=int(input("Enter the number of words to check:"))
print("Enter the word")
for i in range(0,x):
    y=input()
    lis.append(y)
def longest(lis):
    return max(lis,key=len)
print("Lengthy word is'"+longest(lis)+"'")
print("Lenght of the word is ",len(longest(lis)))
