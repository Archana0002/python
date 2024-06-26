str=input("Enter wrods seperated by space: ")
num=int(input("enter the number:"))
c=dict()
str=str.split()
for i in str:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
l=[]
for j in c:
    if c[j]>=num:
        l.append(j)
if len(l)>0:
    print(l)
else:
    print("na")
