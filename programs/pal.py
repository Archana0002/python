def pal(n):
    s=0
    while n > 0:
        d=n%10
        s=s*10+d
        n=n//10
    return s
num=121
f=pal(num)
if(num==f):
    print("palindrome")
else:
    print("not palindrome")
