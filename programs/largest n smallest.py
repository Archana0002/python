my_array=[1,567,999,-6]
if not my_array:
    print("empyt array")
else:
    n=len(my_array)
    max=my_array[0]
    min=my_array[0]
    for i in range(n):
        if(my_array[i]>max):
            max=my_array[i]
        elif(my_array[i]<min):
            min=my_array[i]
        
    print(max)
    print(min)
