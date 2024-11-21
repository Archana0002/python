p=int(input("enetr a number"))
def prime(p):
    if(p<=1):
        return False
    for num in range(2,p):
        if(p%num==0):
            return False
    return True
print(prime(p))

    

    