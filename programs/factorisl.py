
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact = fact *i
    return fact

a=[2,7,5]
l=[]
for num in a:
    s=fact(num)
    l.append(s)
print(l)
