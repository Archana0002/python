a="malayalsam"
rev=""
for i in range(len(a)-1,-1,-1):
    rev=rev+a[i]
print(rev)
if(a==rev):
    print("palindrome")
else:
    print("not palindrome")

