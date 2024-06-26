str=input("Enter alnbhabets and numbers: ")
alpha=[]
num=[]
for i in str:
    if i.isalpha():
        alpha.append(i)
    elif i.isalnum():
        num.append(i)
final=sorted(alpha)+sorted(num)
s=''.join(final)
print(s)
