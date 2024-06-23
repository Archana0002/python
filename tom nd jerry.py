# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
l=[]
while n>0:
        m=input()
        m=int(m,2)
        l.append(m)
        n-=1
print(l,n)
for i in l:
        if i%2 == 0:
                print("tom")
        else:
                print("jerry")
