def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

while True:
    print("CALCULATOR")
    print("1.ADD")
    print("2.SUBTRACT")
    print("3.MULTIPLY")
    print("4.DIVISION")
    print("5.EXIT")

    option = int(input("SELECT A OPERATION: 1,2,3,4,5:"))
    if option == 5 :
        print("exiting program:")
        break
    if option in (1,2,3,4):
        num1=float(input("enter 1st number:"))
        num2=float(input("enter 2nd number:"))
        if option == 1:
            print("result=",add(num1,num2))
        elif option == 2:
            print("result=",sub(num1,num2))
        elif option == 3:
            print("result=",mul(num1,num2))
        elif option == 4:
            print("result=",div(num1,num2))
        else:
            print("invalid option")
    
    
