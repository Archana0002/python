def fun(n):
    print(n)
    b=bin(n)
    b=b[2:len(b)]
    print(b)
    b1=""
    for i in b:
        if i=='1':
            b1=b1+'0'
        else:
            b1=b1+'1'
    print(b1)
    s = 0
    for j in range(len(b1)):
        s = s + (int(b1[j])*(2**(len(b1)-(j+1))))
    return s

print(fun(50))
