def rev(a):
    re=""
    for i in range(len(a)-1,-1,-1):
        re=re+(a[i])
        
    return re


a="malayalam"
print(rev(a))