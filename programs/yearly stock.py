stock=[1,2,3,4,5,6,7,8,9,10,11,12]
num1=5
num2=7
s=0
for i in range(num1-1,num2):
    s+=stock[i]
print(s)


#cache=[1,3,6,10,15,21,28,36,45,55,66,79]      


#       x1,x2,x3,x4
#cache=[x1,x1+x2,x1+x2+x3,x1x2+x3+x4]

