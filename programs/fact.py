'''def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(fact(5))'''


def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact



a = [5 , 2, 6]
l=[]
for num in a:
    s=fact(num)
    print(s)
    l.append(s)
print(l)


