str=input("enter a string")
f=str[0]
str=str.replace(f,'&')
str=f+str[1:]
print("string is",str)