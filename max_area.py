def rect(no,leng):
    arr=[]
    for i in leng:
        if leng.count(i)>=2 and i not in arr:
            arr.append(i)
    max_area=0
    for j in range(len(arr)):
        for k in range(j+1,len(arr)):
            if arr[j]*arr[k]>max_area:
                max_area=arr[j]*arr[k]
    return max_area
                

print(rect(5,[1,8,1,8,8]))
