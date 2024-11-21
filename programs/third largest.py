arr=[9,5]
arr=list(set(arr))
l=len(arr)
if(l<3):
    print("there is no 3 element")
else:
    for i in range(l):
        for j in range(i+1,l):
            if(arr[j]<arr[i]):
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp
    print(arr[-3])

#arr=set(arr)
#arr=sorted(arr)
#n=len(arr)
#print(arr[n-3])