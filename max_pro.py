def pro(arr):
    a=len(arr)
    if a<2:
        print("no such pair")
        return
    a1=arr[0]
    a2=arr[1]
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]*arr[j])>a1*a2:
                a1=arr[i]
                a2=arr[j]
    return a1,a2
            

arr=eval(input("Enter the array:"))
print("maximum is:" ,pro(arr))
