str1=input("enter the first string")
str2=input("enter the second string")
a=str2[0]
b=str1[0]
new_str1=str2[0]+str1[1:]
new_str2=str1[0]+str2[1:]
print(new_str1+' '+new_str2)