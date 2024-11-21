
def fibo(n):
    first=0
    second=1
    print(first)
    for i in range(1,n):
        third = first + second
        print(third)
        first = second
        second = third
    
fibo(7)