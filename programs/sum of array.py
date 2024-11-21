row=int(input("enter number of rows:"))
col=int(input("enter number of columns:"))
matrix=[]
print("enter elements row by row")
for i in range(row):
    row=list(int(map(int,input(f"enter elemennts of row {i+1},seperated by spaces").split())))
    matrix.append(row)

for i,row in enumerate(matrix):
    sums=sum(row)
    print(f"sum of row {i+1}:{sums}")