todo_list=[]
def add():
    item=input("enter a new task:")
    todo_list.append(item)
    print(item + "added to the list")
    
def display():
    print("Todo list")
    for index,item in enumerate(todo_list,start=1):#index start from one
            print(index,"-",item)
def remove():
    display()
    index = int(input("enter number to remove item"))-1
    if 0<= index < len(todo_list):
        removed_item = todo_list.pop(index)
        print(removed_item,"from list")
    else:
        print("invalid")
    
    
while True:
    print("TO-DO LIST APP")
    print("1.ADD TO LIST")
    print("2.DISPLAY LIST")
    print("3.REMOVE FROM LIST")
    print("4.EXIT")
    option = int(input("select a option"))

    if option == 1:
        add()
    elif option == 2:
        display()
    elif option == 3:
        remove()
    elif option == 4:
        print("Exit")
        break
    else:
        print("invalid option selected")
