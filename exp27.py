str=input("Enter a string:")
if (str[-3:]=="ing"):
    str=str.replace(str[-3:],"ly")
else:
    str=str+'ing'
print(str)